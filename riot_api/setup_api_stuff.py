from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os

def setup_enviorment():
    load_dotenv('/Users/kyleriggenbach/Desktop/projects/doubloonin/config2.env')
    # api_key = os.environ['riot_api_key']
    riot_api_key = "RGAPI-6fe6454a-0ae8-471f-8b70-7fe8c3725eb5"
    lol_watcher = LolWatcher(riot_api_key)
    del (riot_api_key)
    return lol_watcher
