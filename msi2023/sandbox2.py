from collections import Counter

my_list = ['Nautilus', 'Olaf', 'Annie', 'Thresh', 'Poppy', 'Jayce', 'Gnar', 'Kennen', 'Annie', 'Annie']

counts = Counter(my_list)

print(counts)

# Convert Counter object to dictionary
counts_dict = dict(counts)

print(counts_dict)
