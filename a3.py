arr = []

with open('/Users/aobalayan/Downloads/dataset_3363_4.txt') as inf:
    for line in inf:
        line = line.strip().lower()
        arr += line.split(';')


dict = {}
ball_math = 0
ball_fizik = 0
ball_rus = 0
for i in range(len(arr)):
    if arr[i].isdigit() == False:
        a = arr[i]
        res_math = arr[i+1]
        res_fizik = arr[i+2]
        res_rus = arr[i+3]
        dict[a] = {res_math, res_fizik, res_rus}
        ball_math += int(res_math)
        ball_fizik += int(res_fizik)
        ball_rus += int(res_rus)
ball = 0

ouf = open('/Users/aobalayan/Downloads/output.txt', 'w')
for key in dict:
    a = dict[key]
    for i in a:
        ball += int(i)
    n = (ball/len(a))
    n = round(n, 9)
    ouf.write(str(n) + '\n')
    ball = 0

ouf.write(str(round(ball_math/len(dict), 9)) + ' ')
ouf.write(str(round(ball_fizik/len(dict), 9)) + ' ')
ouf.write(str(round(ball_rus/len(dict), 9)) + ' ')
