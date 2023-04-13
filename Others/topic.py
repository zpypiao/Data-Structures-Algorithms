3
""" def mysort(li):
    return li[1]
 s = list(input('e').split('\n'))
sss = str('e:\1\aa3.txt 3
e:\3\aa1.txt 2
e:\2\aa2.txt 3
e:\3\aa1.txt 1
e:\1\aa1.txt 3
e:\3\aa1.txt 2
e:\1\aa3.txt 3
e:\2\aa3.txt 2
e:\1\aa1.txt 2
e:\3\aa3.txt 2
e:\1\aa2.txt 2
e:\1\aa3.txt 1
e:\1\aa3.txt 1
e:\2\aa3.txt 2
e:\1\aa2.txt 1
e:\3\aa1.txt 2
e:\1\aa1.txt 3
e:\2\aa1.txt 1
e:\3\aa3.txt 2
e:\1\aa1.txt 1
e:\2\aa2.txt 2
e:\3\aa3.txt 2
e:\1\aa2.txt 1
e:\1\aa3.txt 2
e:\1\aa3.txt 3
e:\1\aa2.txt 3
e:\3\aa1.txt 3
e:\2\aa2.txt 2
e:\1\aa1.txt 1
e:\2\aa3.txt 1
e:\3\aa1.txt 1
e:\2\aa1.txt 3
e:\3\aa3.txt 2
e:\1\aa3.txt 3
e:\2\aa3.txt 3
e:\1\aa2.txt 3
e:\2\aa2.txt 1
e:\1\aa3.txt 1
e:\1\aa3.txt 1
e:\3\aa3.txt 3
e:\3\aa3.txt 2
e:\1\aa2.txt 3
e:\1\aa2.txt 3
e:\1\aa2.txt 3
e:\1\aa1.txt 1
e:\2\aa3.txt 1
e:\3\aa3.txt 1
e:\2\aa3.txt 2
e:\3\aa1.txt 3
e:\2\aa2.txt 2
e:\2\aa2.txt 2
e:\2\aa3.txt 1
e:\1\aa3.txt 3
e:\3\aa1.txt 2
e:\3\aa2.txt 2
e:\1\aa2.txt 1
e:\2\aa2.txt 1
e:\2\aa1.txt 2
e:\2\aa2.txt 1
e:\1\aa2.txt 1
e:\2\aa3.txt 1
e:\2\aa2.txt 1
e:\2\aa1.txt 2
e:\3\aa2.txt 3
e:\3\aa1.txt 3
e:\2\aa2.txt 3
e:\2\aa3.txt 1
e:\3\aa3.txt 2
e:\2\aa3.txt 1
e:\1\aa1.txt 2
e:\3\aa3.txt 1
e:\3\aa1.txt 1
e:\2\aa2.txt 3
e:\3\aa3.txt 2
e:\2\aa1.txt 3
e:\1\aa3.txt 3
e:\3\aa2.txt 1
e:\2\aa1.txt 3
e:\1\aa3.txt 3
e:\2\aa2.txt 2
e:\1\aa1.txt 2
e:\3\aa1.txt 1
e:\1\aa3.txt 1
e:\3\aa1.txt 2
e:\1\aa1.txt 2
e:\1\aa1.txt 3
e:\3\aa1.txt 1
e:\3\aa1.txt 1
e:\2\aa3.txt 3
e:\2\aa2.txt 1
e:\2\aa1.txt 2
e:\2\aa2.txt 1
e:\3\aa2.txt 3
e:\1\aa2.txt 1
e:\3\aa2.txt 2
e:\2\aa1.txt 1
e:\2\aa3.txt 3
e:\1\aa1.txt 2
e:\1\aa1.txt 1
e:\1\aa1.txt 2')
s = list(sss.split('\\'))
res = []
count = []
for each in s:
    s1 = list(each.split('\\'))[-1]
    s2, s3 = s1.split(' ')
    if (len(s2)) > 16:
        s2 = s2[-16:]
    s2 = s2 + ' '+s3
    if s2 in res:
        count[res.index(s2)] += 1
    else:
        res.append(s2)
        count.append(1)
result = []
for i in range(len(count)):
    result.append([res[i], count[i]])
result.sort(key=mysort, reverse=True)
for i in range(len(result)):
    if i <= 8:
        print(result[i][0], result[i][1]) """


# 1. five functions
""" c = list(int(i) for i in input().split())
board = 0
temp = 0
select = 0
for ele in c:
    if ele == 1:
        board = board - select + 1
        select = 0
    elif ele == 2:
        temp = select
    elif ele == 3:
        temp = select
        board -= select
        select = 0
    elif ele == 4:
        board = board - select + temp
        select = 0
    else:
        select = board
    print(board)
print(board) """
        
# 2. minus two number
""" def decode(string, n):
    res = 0
    k = 1
    for i in range(len(string)-1, -1, -1):
        m = string[i]
        if ord(m) >= ord('0') and ord(m)<=ord('9'):
            res += int(m)*k
        else:
            res += (ord(m)-ord('a')+10)*k
        k *= n
    return res

def encode(num, n):
    string = ''
    while num:
        string = str(num % n)+string
        num = num // n
    return string

def check(string):
    if string[0] == '0' and len(string)>1:
        return False
    else:
        return True
n, a, b = input().split()
n = int(n)
if check(a) and check(b):
    num1, num2 = decode(a, n), decode(b, n)
    res = num1 - num2
    if res >= 0:
        print(0,encode(res, n))
    else:
        print(-1, encode(abs(res, n)))
else:
    print(-1) """

# 3. decode TLV

# 4. VLAN
""" def translate(li):
    res = []
    for each in li:
        if '-' in each:
            a, b = each.split('-')
            a = int(a)
            b = int(b)
            for i in range(a, b+1):
                res.append(i)
        else:
            a = int(each)
            res.append(a)
    res.sort()
    return res

def detranslate(li):
    li.append(-1000)
    left = 0
    right = 0
    res = []
    for i in range(len(li)-1):
        if li[i+1] == li[i]+1:
            right += 1
        else:
            if right == left:
                res.append(str(li[left]))
            else:
                res.append(str(li[left])+'-'+str(li[right]))
            left = i+1
            right = i+1
    return res
wl = list(input().split(' '))
val = int(input())

li = translate(wl)
if val in li:
    ind = li.index(val)
    li.pop(ind)

res = detranslate(li)
print(res) """

# 5. highth and weighth
""" li = []
m = int(input())
high = list(int(i) for i in input().split())
weight = list(int(i) for i in input().split())
for i in range(m):
    li.append((i+1, high[i], weight[i]))
li.sort(key=lambda x:(x[1], x[2], x[0]))
for i in li:
    print(i[0]) """

# 6. reverse sentence
""" string = list(input().split())
a, b = (int(i) for i in input().split())
if a<=len(string)-1 and b<=len(string)-1 and a<=b:
    k = string[a: b+1]
    k.reverse()
    string[a: b+1] = k
    res = ''
    for i in range(len(string)-1):
        res = res+string[i]+' '
    res+=string[-1]
    print(res)
else:
    print('ERROR') """

# 7. count game
""" m = int(input())
if m<=1 or m>=100:
    print('ERROR')
else:
    k = 1
    p = 0
    de = 0
    li = [i+1 for i in range(100)]
    while True:
        if li[p]:
            if k == m:
                li[p] = 0
                k = 1
                de += 1
                if de == 101-m:
                    break
            else:
                k += 1
        p = (p+1)%100
    res = []
    for i in range(len(li)):
        if li[i]:
            res.append(i+1)
    print(res) """

# 8. judge
""" status = True
m, n = (int(i) for i in input().split())
if m<3 or m>10 or n<3 or n>100:
    status = False
score_m = []
for i in range(m):
    score_m.append(list(int(i) for i in input().split()))
score_n = []
for i in range(n):
    score_n.append([])
    for j in range(m):
        if score_m[j][i]<1 or score_m[j][i]>10:
            status = False
        score_n[i].append(score_m[j][i])
if status:
    for i in range(n):
        score_n[i].append(sum(score_n[i]))
        score_n[i].sort(reverse=True)
        score_n[i].append(i+1)
    score_n.sort(key=lambda x:tuple(x[i] for i in range(m)), reverse=True)
    for i in range(3):
        print(score_n[i][-1])
else:
    print(-1) """

# 9. stable signal
""" n = int(input())
li = list(int(i) for i in input().split())
res = []
k = 0
for i in range(len(li)):
    if k == 0 and li[i]<=n:
        left = i
        k = 1
    elif k == 0 and li[i]>n:
        continue
    elif sum(li[left:i+1])/(i+1-left)>n:
        right = i-1
        if left == right:
            res.append(str(left))
        else:
            res.append(str(left)+'-'+str(right))
        k = 0
    elif i == len(li)-1:
        right = i
        if left == right:
            res.append(str(left))
        else:
            res.append(str(left)+'-'+str(right))
print(res) """

# 10. mass and mid
""" def mass(li):
    s = set(li)
    res = []
    for each in s:
        if li.count(each)-1:
            res.append(each)
    return res

def mid(li):
    li.sort()
    m = len(li)//2
    if len(li)%2:
        return li[m]
    else:
        return (li[m]+li[m])/2
li = list(int(i) for i in input().split())
res = mass(li)
print(mid(res)) """

# 11. content sort
""" def calculat(string):
    res = 0
    left = 0
    right = 0
    for i in range(len(string)):
        if ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9'):
            continue
        else:
            right = i
            num = int(string[left:right])
            if string[i] == 'T':
                k = 1024*1024
            elif string[i] == 'G':
                k = 1024
            else:
                k =1
            res += num*k
            left = i+1
    return res

n = int(input())
li = []
for _ in range(n):
    li.append(input())
li.sort(key=calculat)
print(li) """

# 12. word link
""" def mysort(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if len(li[j+1])<len(li[j]):
                continue
            elif len(li[j+1])>len(li[j]):
                li[j+1], li[j] = li[j], li[j+1]
            else:
                for k in range(len(li[j])):
                    if ord(li[j+1][k]) < ord(li[j][k]):
                        li[j+1], li[j] = li[j], li[j+1]
                        break
start = int(input())
n = int(input())
li = []
for i in range(n):
    li.append(input())
string = li.pop(start)
while True:
    s = string[-1]
    temp = []
    for each in li:
        if each[0] == s:
            temp.append(each)
    if temp == []:
        break
    else:
        mysort(temp)
        string += temp[0]
        li.pop(li.index(temp[0]))

print(string) """

# 12. no.k
""" def cal(num):
    if num>1:
        return num*(num-1)
    elif num == 0:
        return 1
    else:
        return num

m = int(input())
n = int(input())-1
k = m-1

li = list(str(i+1) for i in range(m))
li.sort(reverse=True)
res = ''

for i in range(k, -1, -1):
    a = n//cal(i)+1
    b = n%cal(i)
    res += li.pop(-a)
    n = b
print(res) """

# 13. order
