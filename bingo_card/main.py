import random

bingo_items = [
    {'thing': '1', 'status': False},
    {'thing': '2', 'status': False},
    {'thing': '3', 'status': False},
    {'thing': '4', 'status': False},
    {'thing': '5', 'status': False},
    {'thing': '6', 'status': True},
    {'thing': '7', 'status': False},
    {'thing': '8', 'status': False},
    {'thing': '9', 'status': False},
    {'thing': '10', 'status': True},
    {'thing': '11', 'status': False},
    {'thing': '12', 'status': False},
    {'thing': '13', 'status': True},
    {'thing': '14', 'status': False},
    {'thing': '15', 'status': False},
    {'thing': '16', 'status': False},
    {'thing': '17', 'status': False},
    {'thing': '18', 'status': False},
    {'thing': '19', 'status': False},
    {'thing': '20', 'status': False},
    {'thing': '21', 'status': True},
    {'thing': '22', 'status': False},
    {'thing': '23', 'status': True},
    {'thing': '24', 'status': False},
    {'thing': '25', 'status': True},
    {'thing': '26', 'status': False},
    {'thing': '27', 'status': False},
    {'thing': '28', 'status': False},
    {'thing': '29', 'status': False},
    {'thing': '30', 'status': False},
    {'thing': '31', 'status': True},
    {'thing': '32', 'status': True},
    {'thing': '33', 'status': False}
]

random_items = random.sample(bingo_items, 24)

grid = [
    [
        {'thing': random_items[0]['thing'], 'status': random_items[0]['status']},
        {'thing': random_items[1]['thing'], 'status': random_items[1]['status']},
        {'thing': random_items[2]['thing'], 'status': random_items[2]['status']},
        {'thing': random_items[3]['thing'], 'status': random_items[3]['status']},
        {'thing': random_items[4]['thing'], 'status': random_items[4]['status']},
    ],
    [
        {'thing': random_items[5]['thing'], 'status': random_items[5]['status']},
        {'thing': random_items[6]['thing'], 'status': random_items[6]['status']},
        {'thing': random_items[7]['thing'], 'status': random_items[7]['status']},
        {'thing': random_items[8]['thing'], 'status': random_items[8]['status']},
        {'thing': random_items[9]['thing'], 'status': random_items[9]['status']},
    ],
    [
        {'thing': random_items[10]['thing'], 'status': random_items[10]['status']},
        {'thing': random_items[11]['thing'], 'status': random_items[11]['status']},
        {'thing': 'FREE', 'status': True},
        {'thing': random_items[12]['thing'], 'status': random_items[12]['status']},
        {'thing': random_items[13]['thing'], 'status': random_items[13]['status']},
    ],
    [
        {'thing': random_items[14]['thing'], 'status': random_items[14]['status']},
        {'thing': random_items[15]['thing'], 'status': random_items[15]['status']},
        {'thing': random_items[16]['thing'], 'status': random_items[16]['status']},
        {'thing': random_items[17]['thing'], 'status': random_items[17]['status']},
        {'thing': random_items[18]['thing'], 'status': random_items[18]['status']},
    ],
    [
        {'thing': random_items[19]['thing'], 'status': random_items[19]['status']},
        {'thing': random_items[20]['thing'], 'status': random_items[20]['status']},
        {'thing': random_items[21]['thing'], 'status': random_items[21]['status']},
        {'thing': random_items[22]['thing'], 'status': random_items[22]['status']},
        {'thing': random_items[23]['thing'], 'status': random_items[23]['status']},
    ]
]

print(grid)

f = open(f"publishes/grid.txt", "a")

opening = f'|B|I|N|G|O| \n' \
          '|-|-|-|-|-| \n'
f.write(opening)


for index1, column in enumerate(grid):

    test1 = grid[index1][0]["status"]
    text1 = grid[index1][0]["thing"]
    if test1:
        text1 = f'🔴~~{grid[index1][0]["thing"]}~~'

    test2 = grid[index1][1]["status"]
    text2 = grid[index1][1]["thing"]
    if test2:
        text2 = f'🔴~~{grid[index1][1]["thing"]}~~'

    test3 = grid[index1][2]["status"]
    text3 = grid[index1][2]["thing"]
    if test3:
        text3 = f'🔴~~{grid[index1][2]["thing"]}~~'

    test4 = grid[index1][3]["status"]
    text4 = grid[index1][3]["thing"]
    if test4:
        text4 = f'🔴~~{grid[index1][3]["thing"]}~~'

    test5 = grid[index1][4]["status"]
    text5 = grid[index1][4]["thing"]
    if test5:
        text5 = f'🔴~~{grid[index1][4]["thing"]}~~'

    string = f'|{text1}|{text2}|{text3}|{text4}|{text5}| \n'
    f.write(string)


for index1, column in enumerate(grid):
    if grid[index1][4]["status"]:
        pass

# todo: save each randomy gnerated grid into database/file along with (user, link, win/loss boolean)



