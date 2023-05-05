from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os

def setup_enviorment():
    load_dotenv('/Users/kyleriggenbach/Desktop/projects/doubloonin/config2.env')
    # api_key = os.environ['riot_api_key']
    riot_api_key = "RGAPI-53a81852-103d-48e9-9dd0-24cc9a35df72"
    lol_watcher = LolWatcher(riot_api_key)
    del (riot_api_key)
    return lol_watcher