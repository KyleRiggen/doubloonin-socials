# removing duplicated from the list using naive methods

# initializing list
sam_list = [11, 13, 15, 16, 13, 15, 16, 11]
print ("The list is: " + str(sam_list))

# remove duplicated from list
result = []
for i in sam_list:
    if i not in result:
        result.append(i)
    else:
        print(f'removed: {i}')

# printing list after removal
print ("The list after removing duplicates : " + str(result))