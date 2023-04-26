import json

with open("jsons/output.json", "r") as infile:
    data = json.load(infile)

url_end = {
    'deathknight/blood': 0,
    'deathknight/frost': 0,
    'deathknight/unholy': 0,
    'demonhunter/havoc': 0,
    'demonhunter/vengeance': 0,
    'druid/balance': 0,
    'druid/feral': 0,
    'druid/guardian': 0,
    'druid/restoration': 0,
    'evoker/devastation': 0,
    'evoker/preservation': 0,
    'hunter/beastmastery': 0,
    'hunter/survival': 0,
    'hunter/marksmanship': 0,
    'mage/arcane': 0,
    'mage/fire': 0,
    'mage/frost': 0,
    'monk/brewmaster': 0,
    'monk/mistweaver': 0,
    'monk/windwalker': 0,
    'paladin/holy': 0,
    'paladin/protection': 0,
    'paladin/retribution': 0,
    'priest/discipline': 0,
    'priest/holy': 0,
    'priest/shadow': 0,
    'rogue/assassination': 0,
    'rogue/outlaw': 0,
    'rogue/subtlety': 0,
    'shaman/elemental': 0,
    'shaman/enhancement': 0,
    'shaman/restoration': 0,
    'warlock/affliction': 0,
    'warlock/demonology': 0,
    'warlock/destruction': 0,
    'warrior/arms': 0,
    'warrior/fury': 0,
    'warrior/protection': 0,
}

first_100_items = data[:1000]
summary = {}
for player in first_100_items:
    for spec in url_end:
        if player['class_spec'] == spec:
            url_end[spec] = url_end[spec] + 1

print(url_end)
sorted_dict = dict(sorted(url_end.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)

cleaned = {}
for key, value in sorted_dict.items():
    words = key.split('/')
    words = [word.capitalize() for word in words]
    new_key = ' '.join(words)
    cleaned[new_key] = value

print(cleaned)

# Open a file for writing
with open("jsons/summary.json", "w") as outfile:
    # Convert the Python variable to JSON and write it to the file
    json.dump(cleaned, outfile)