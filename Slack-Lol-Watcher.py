from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time
import requests

lol_watcher = LolWatcher('Your_Riot_API_Key') # Riot API Key
my_region = 'kr' # 서버 위치
watcher_Target = 'Watcher_Target' # Watcher 대상
myToken = 'Your_Slack_Token' # Slack API Token
channel = '#Your_Channel' # Slack 채널

me = lol_watcher.summoner.by_name(my_region, watcher_Target)

# Slack API
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

spectator = None

while True:
    print('[*] Checking...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        if datetime.now() - start_time < timedelta(minutes=5):
            notice_print = (f'[!] [{watcher_Target}] Playing game!', start_time.strftime('%Y-%m-%d %H:%M:%S'))
            print(notice_print)
            post_message(myToken,channel,notice_print)
            time.sleep(300)
    except:
        pass

    time.sleep(5)