arr = []

with open('/Users/aobalayan/Downloads/dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip().lower()
        arr += line.split(' ')

dict = {}

for i in arr:
    a = arr.count(i)
    if i not in dict:
        dict[i] = a


slovar_values = set()
for value in dict.values():
    slovar_values.add(value)

max_values = max(slovar_values)
slovar_keys = set()
for key, value in dict.items():
    if value == max_values:
        slovar_keys.add(key)

print(min(slovar_keys), max_values)