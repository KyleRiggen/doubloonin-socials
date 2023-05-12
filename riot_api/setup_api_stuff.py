from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os

def setup_enviorment():
    load_dotenv('/Users/kyleriggenbach/Desktop/projects/doubloonin/config2.env')
    # api_key = os.environ['riot_api_key']
    riot_api_key = "RGAPI-f825241c-9f98-423b-a31a-7a75c9910897"
    lol_watcher = LolWatcher(riot_api_key)
    del (riot_api_key)
    return lol_watcher