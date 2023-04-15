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
""" dirs = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, 'A':12, '2':15}
li = list(input().split())
li.sort(key = lambda s:dirs[s])
temp = li.pop(0)
res = []
p = 0
while len(li):
    if dirs[li[p]] == dirs[temp.split()[-1]]+1:
        temp = temp + ' ' +li.pop(p)
        if len(li) == 0 and len(temp)>=9:
            res.append(temp)
    elif dirs[li[p]] == dirs[temp.split()[-1]]:
        if p != len(li)-1:
            p += 1
        else:
            if len(temp)>=9:
                res.append(temp)
            if len(li):
                temp = li.pop(0)
                p = 0
            else:
                break
    else:
        if len(temp)>=9:
            res.append(temp)
        if len(li):
            temp = li.pop(0)
            p = 0
        else:
            break
print(res) """

# 14. non-strict add number order
""" string = input()
big = 0
former = 0
count = 0
for i in range(len(string)):
    if count == 0 and ord(string[i])>=ord('0') and ord(string[i])<=ord('9'):
        m = int(string[i])
        former = m
        count += 1
    elif count == 0:
        continue
    elif ord(string[i])>=ord('0') and ord(string[i])<=ord('9'):
        m = int(string[i])
        if m >= former:
            count += 1
            former = m
        else:
            if count > big:
                big = count
            count = 0
    else:
        if count > big:
            big = count
        count = 0
print(big) """

# 14. classify
""" res = ['', '']
p = 0
student = list(input().split())
print(student)
res[p] += student.pop(0).split('/')[0]
for i in range(len(student)):
    if student[i].split('/')[1] == 'N':
        p = (p+1)%2
    res[p] = res[p] + ' ' +student[i].split('/')[0]
for each in res:
    print(each) """

# 15. dispatch
""" num = int(input())
b = 0
while True:
    if num <= 2**b:
        break
    else:
        b += 1
a = b-1
left = num-2**a
right = 2**b-num
big = right+b
small = left+a
res = min(big, small)
print(res) """

# 15. sort
""" li = list(int(i) for i in input().split())
c = -1
for i in range(len(li)-1):
    if (li[i]-li[i+1])*c >= 0:
        li[i], li[i+1] = li[i+1], li[i]
    c *= -1
print(li) """

# 16. the smallest longth
""" x, y = (int(i) for i in input().split())
multiply = 26**y
res = 0
while True:
    if (10**res)*multiply>=x:
        break
    else:
        res += 1
if res:
    print(res)
else:
    print(1) """

# 17. x**2 + y**2 = z**2
""" def check(a, b, c):
    for i in range(2, min(a,b)+1):
        if a%i==0 and b%i==0:
            return False
    for i in range(2, min(a,c)+1):
        if a%i==0 and c%i==0:
            return False
    for i in range(2, min(b,c)+1):
        if b%i==0 and c%i==0:
            return False
    return True
low = int(input())
high = int(input())
res = []
for i in range(low, high-1):
    for j in range(i+1, high+1):
        m = (i**2+j**2)**0.5
        if m-int(m) == 0 and m<=high and check(i, j, int(m)):
            res.append((i, j, int(m)))
if len(res):
    print(res)
else:
    print('NA') """

# 18. when i meet seven
""" principle = list(int(i) for i in input().split())
n = len(principle)
m = sum(principle)
location = []
start = 1
count = 0
while count < m:
    if start%7==0 or '7' in str(start):
        location.append(start)
        count += 1
    start += 1
res = [0 for _ in range(n)]
for each in location:
    res[each%n-1] += 1
print(res) """

# 19. a monkey is climbing a mountain
""" def cmn(m, n):
    def selfmulitiply(n):
        if n>2:
            return selfmulitiply(n-1)*n
        elif n ==2:
            return 2
        else:
            return 1
    return selfmulitiply(m)/(selfmulitiply(n)*selfmulitiply(m-n))

n = int(input())
res = 0
k = n//3
for i in range(k+1):
    a = i
    b = n-i*3
    res += cmn(a+b, a)
res = int(res)
print(res) """

# 20. the max of a moving window
""" n = int(input())
li = [int(i) for i in input().split()]
m = int(input())
res = 0
for i in range(n-m+1):
    temp = sum(li[i:i+m])
    if temp > res:
        res = temp
print(res) """

# 21. the calculation of unknown code
""" def well(x, y):
    return 2*x+3*y+4
def dollar(x, y):
    return 3*x+y+2
string = input()
well_divide = string.split('#')
for i in range(len(well_divide)):
    dollar_devide = [int(i) for i in well_divide[i].split('$')]
    temp = dollar_devide[0]
    for j in range(1, len(dollar_devide)):
        temp = dollar(temp, dollar_devide[j])
    well_divide[i] = temp
temp = well_divide[0]
for i in range(1, len(well_divide)):
    temp = well(temp, well_divide[i])

print(temp) """

# 22. calculate the area
""" n, determine = (int(i) for i in input().split())
li = []
for i in range(n):
    li.append(tuple(int(i) for i in input().split()))
res = 0
x = 0
lx = 0
y = 0
for each in li:
    lx = each[0] - x
    res += abs(lx*y)
    y = y + each[1]
    x = each[0]
lx = determine - x
res += abs(lx*y)
print(res) """

# 23. calculate the max multiply
""" def issimmulate(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    for each in set1:
        if each in set2:
            return True
    return False

li = input().split(',')
res = 0
for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if not issimmulate(li[i], li[j]):
            m = len(li[i])*len(li[j])
            if m>res:
                res = m
print(res) """

# 24. check whether exist the rank which can meet the demand
""" n = int(input())
nums = tuple(int(i) for i in input().split())
res = 0
c = 0
for i in range(n):
    for j in range(n):
        if i != j and nums[i]+2*nums[j] in nums and nums.index(nums[i]+2*nums[j]) not in [i, j]:
            res = tuple((nums[i]+2*nums[j], nums[i], nums[j]))
            c = 1
            break
    if c:
        break
if res:
    print(res)
else:
    print(0) """

# 25. the extend of a matrix
""" import copy
ref = tuple(int(i) for i in input().split())
target = ref[0]*ref[1]
matrix_a = [list(0 for _ in range(ref[1])) for _ in range(ref[0])]
matrix_a[ref[2]][ref[3]] = 1
matrix_a[ref[4]][ref[5]] = 1
matrix = copy.deepcopy(matrix_a)
print(matrix)
time = 0
while True:
    for i in range(ref[0]):
        for j in range(ref[1]):
            if matrix[i][j] == 1:
                if i-1 >= 0:
                    matrix_a[i-1][j] = 1
                if i+1<=ref[1]-1:
                    matrix_a[i+1][j] = 1
                if j-1 >= 0:
                    matrix_a[i][j-1] = 1
                if j+1 <= ref[0]-1:
                    matrix_a[i][j+1] = 1
    matrix = copy.deepcopy(matrix_a)
    print(matrix)
    time += 1
    temp = sum([sum(i) for i in matrix])
    if temp == target:
        break
print(time) """

# 26. the max value of matrix
""" def decode(string):
    m = 1
    res = 0
    for i in range(len(string)-1, -1, -1):
        res += m*int(string[i])
        m *= 2
    return res

def max_decode(string):
    res = 0
    for _ in range(len(string)):
        m = decode(string)
        if m> res:
            res = m
        string = string[-1] + string[:-1]
    return res

n = int(input())
li = []
for _ in range(n):
    s = ''
    for i in input().split():
        s += i
    li.append(s)

res = 0
for each in li:
    m = max_decode(each)
    res += m
print(res) """

# 27. the life of a worker
""" def break_one(li):
    if li.count('absent') > 1:
        return True
    else:
        return False

def break_two(li):
    for i in range(len(li)):
        if li[i] == 'late' or li[i] == 'leaveearly':
            li[i] = 1
        else:
            li[i] = 0
    for i in range(len(li)-1):
        if li[i]*li[i+1]:
            return True
    return False

def break_three(li):
    for i in range(len(li)):
        if li[i] in ['absent', 'late', 'leaveearly']:
            li[i] = 1
        else:
            li[i] = 0
    if len(li) <= 7:
        if sum(li) <= 3:
            return False
        else:
            return True
    else:
        for i in range(len(li)-6):
            if sum(li[i:i+7]) > 3:
                return True
        return False

n = int(input())
res = []
for _ in range(n):
    li = input().split()
    if break_one(li) or break_two(li) or break_three(li):
        res.append(False)
    else:
        res.append(True)

print(res) """