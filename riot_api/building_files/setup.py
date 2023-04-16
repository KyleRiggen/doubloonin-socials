from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os

def setup_enviorment():
    load_dotenv('/Users/kyleriggenbach/Desktop/projects/doubloonin/config2.env')
    api_key = os.environ['riot_api_key']
    lol_watcher = LolWatcher(api_key)
    del (api_key)
    return lol_watcher