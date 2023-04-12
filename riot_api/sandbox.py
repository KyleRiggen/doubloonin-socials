array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)
new_array = []
for num in array:
    if num > 5:
        new_array.append(num)

print(new_array)