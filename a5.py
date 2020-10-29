import requests


inf = open('/Users/aobalayan/Downloads/dataset_3378_3.txt')
url = inf.readline().strip()
inf.close()

f = open(r'/Users/aobalayan/Downloads/314.txt', "wb")
ufr = requests.get(url)
f.write(ufr.content)
f = open(r'/Users/aobalayan/Downloads/314.txt', "r")
text = f.readline().strip()

while text[0:2] != 'We':
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + text
    f = open(r'/Users/aobalayan/Downloads/' + text, "w")
    ufr = requests.get(url)
    a = ufr.text
    s = (ufr.text)
    f.write(s)
    f = open(r'/Users/aobalayan/Downloads/' + text, "r")
    text = f.readline().strip()
    print(text)

print(a)