
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

filter = dict()

for item in items:
    filter[item] = 0

result = set(filter.keys())
print(result)
