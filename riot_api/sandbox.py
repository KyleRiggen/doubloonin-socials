dicts = {}
values = ["Hi", "I", "am", "John"]

for i in values:
    dicts[i] = values[i]
print(dicts)

# In [7]: dict(list(enumerate(values)))
# Out[7]: {0: 'Hi', 1: 'I', 2: 'am', 3: 'John'}