from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os

def setup_enviorment():
    load_dotenv('/Users/kyleriggenbach/Desktop/projects/doubloonin/config2.env')
    # api_key = os.environ['riot_api_key']
    riot_api_key = "RGAPI-2b07e4bc-2bd8-4f6f-b230-8f8f5ce44bc8"
    lol_watcher = LolWatcher(riot_api_key)
    del (riot_api_key)
    return lol_watcher