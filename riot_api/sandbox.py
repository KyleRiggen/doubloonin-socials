from config_variables import *
from doubloonin.riot_api.building_files.setup import *

lol_watcher = setup_enviorment()
queue_type = 'RANKED_SOLO_5x5'
data2 = config['points']
challenger_ladder = lol_watcher.league.challenger_by_queue(region='na1', queue=queue_type)


print(challenger_ladder)