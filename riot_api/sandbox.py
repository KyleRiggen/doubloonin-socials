champs = {
    "data": {
        "Aatrox": {
            "id": "Aatrox",
            "key": "266",
            "name": "Aatrox",
        },
        "Ahri": {
            "id": "Ahri",
            "key": "103",
            "name": "Ahri",
        },
        "MonkeyKing": {
            "id": "MonkeyKing",
            "key": "84",
            "name": "Wukong",
        }
    }
}

champStats = {
    "Tryndamere": {
        "kills": 1,
        "deaths": 3,
        "assists": 1
    },
    "Ryze": {
        "kills": 2,
        "deaths": 3,
        "assists": 2
    },
    "MonkeyKing": {
        "kills": 21,
        "deaths": 14,
        "assists": 21
    }
}

for key in champs['data']:
    if key != champs['data'][key]['name']:
        replacement = champs['data'][key]['name']
        values = champStats[key]
        champStats[replacement] = values
        del champStats[key]

print(champStats)
