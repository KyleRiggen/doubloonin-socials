incoming_data = ['billy', 'kyle', 'newItem', 'anotherItem', 'billy', 'kyle']
resulting_data = {}

for item in incoming_data:
    total = 0

    if item not in resulting_data.keys():
        resulting_data[item] = 1
    else:
        total = resulting_data[item] + 1
        resulting_data[item] = total

print(resulting_data)