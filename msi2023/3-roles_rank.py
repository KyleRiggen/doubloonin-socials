import json

def get_rank_change(role):
    with open(f'/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-roles_{role}.json') as user_file:
        file_contents = user_file.read()
    new_json = json.loads(file_contents)

    with open(f'/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-roles_{role}_keep.json') as user_file:
        file_contents = user_file.read()
    yesterday = json.loads(file_contents)

    for index, champ in enumerate(new_json):
        new_json[champ]['rank'] = index + 1

    for champ in yesterday:
        for champ2 in new_json:
            if champ2 == champ:
                print(yesterday[champ]['rank'] - new_json[champ2]['rank'])
                new_json[champ2]['rankChange'] = yesterday[champ]['rank'] - new_json[champ2]['rank']

    default_rankChange = 0  # default value for rankChange

    for item in new_json.values():
        if isinstance(item, dict):  # check if item is a dictionary
            item.setdefault('rankChange', default_rankChange)
        else:  # if item is not a dictionary, skip it
            continue

    with open(f'/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-roles_{role}.json', 'w',
              encoding='utf-8') as f:
        json.dump(new_json, f, ensure_ascii=False, indent=4)

get_rank_change('top')
get_rank_change('jungle')
get_rank_change('mid')
get_rank_change('bot')
get_rank_change('sup')