inf = open('/Users/aobalayan/Downloads/dataset_3363_2.txt')

s1 = inf.readline().strip()
inf.close()

s1 = s1 + ' '
bukva = ''
chislo = ''
a=''
for i in range(len(s1)-1):
    if s1[i].isdigit() == False:
        bukva = s1[i]
        i += 1
        while s1[i].isdigit():
            chislo += s1[i]
            i += 1
        a += bukva * int(chislo)
        chislo = ''

ouf = open('/Users/aobalayan/Downloads/output.txt', 'w')
ouf.write(a)