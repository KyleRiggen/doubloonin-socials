ratings = [1, 2, 3, 4, 5, 6]
names = ['bily', 'bob', 'phil', 'sil', 'frank', 'bob']
goal = []

for index, rating in enumerate(ratings):
    info = {
        'rating': rating,
        'name': names[index]
    }
    goal.append(info)

print(goal)