data = {"K'Sante": {'kills': 9, 'deaths': 12, 'assists': 19, 'score': 13, 'rank': 1, 'rankChange': 3},
        'Karma': {'kills': 2, 'deaths': 1, 'assists': 8, 'score': 10, 'rank': 2},
        'Fiora': {'kills': 3, 'deaths': 3, 'assists': 7, 'score': 7, 'rank': 3, 'rankChange': -1},
        'rankChange': 0}

default_rankChange = 0  # default value for rankChange

for item in data.values():
    if isinstance(item, dict):  # check if item is a dictionary
        item.setdefault('rankChange', default_rankChange)
    else:  # if item is not a dictionary, skip it
        continue

print(data)