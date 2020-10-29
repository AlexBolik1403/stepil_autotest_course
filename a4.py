import requests


inf = open('/Users/aobalayan/Downloads/dataset_3378_2.txt')
url = inf.readline().strip()
inf.close()

f = open(r'/Users/aobalayan/Downloads/314.txt', "wb")
ufr = requests.get(url)
f.write(ufr.content)

stroki = []
with open('/Users/aobalayan/Downloads/314.txt') as inf2:
    for line in inf2:
        line = line.strip().splitlines()
        stroki.append(line)

print(len(stroki))