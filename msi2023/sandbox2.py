list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

new_list = [x for x in list1 if x in list2]

print(new_list) # Output: [2, 4]