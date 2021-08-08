from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time

lol_watcher = LolWatcher('Your_Riot_API_Key') # Riot API Key

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, 'Watcher_Target') # Watcher 대상

spectator = None

while True:
    print('[*] Checking...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        if datetime.now() - start_time < timedelta(minutes=5):
            print('[!] Playing game!', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass

    time.sleep(5)