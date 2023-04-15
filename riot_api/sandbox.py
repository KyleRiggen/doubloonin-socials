champStats = {
    "Yasuo": {
        "kills": 49,
        "deaths": 43,
        "assists": 49,
        "wins": 6,
        "losses": 3,
        "score": 140
    },
    "Syndra": {
        "kills": 16,
        "deaths": 15,
        "assists": 16,
        "wins": 0,
        "losses": 3,
        "score": 4
    },
    "Taric": {
        "kills": 11,
        "deaths": 22,
        "assists": 11,
        "wins": 3,
        "losses": 2,
        "score": 10
    },
    "Malphite": {
        "kills": 8,
        "deaths": 1,
        "assists": 8,
        "wins": 1,
        "losses": 0,
        "score": 40
    },
    "Yone": {
        "kills": 3,
        "deaths": 5,
        "assists": 3,
        "wins": 0,
        "losses": 1,
        "score": -8
    },
    "Rakan": {
        "kills": 23,
        "deaths": 70,
        "assists": 23,
        "wins": 8,
        "losses": 6,
        "score": -28
    },
    "Xin Zhao": {
        "kills": 5,
        "deaths": 8,
        "assists": 5,
        "wins": 0,
        "losses": 1,
        "score": -6
    },
    "Vayne": {
        "kills": 19,
        "deaths": 7,
        "assists": 19,
        "wins": 0,
        "losses": 1,
        "score": 52
    },
    "Senna": {
        "kills": 4,
        "deaths": 12,
        "assists": 4,
        "wins": 1,
        "losses": 0,
        "score": 2
    },
    "Jax": {
        "kills": 33,
        "deaths": 12,
        "assists": 33,
        "wins": 3,
        "losses": 2,
        "score": 118
    }
}



def get_top_scores(champStats):
    list_champs = [(name,champStats[name]['score']) for name in champStats]
    sorted_champs = sorted(list_champs,key=lambda x: x[1],reverse = True)
    print(sorted_champs)
    ret_dict = {}
    for champ,kills in sorted_champs[:3]:
        ret_dict[champ] = kills

    return ret_dict

print(get_top_scores(champStats))
