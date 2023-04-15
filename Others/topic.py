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

# 28. a reliable car
""" def translate(num):
    def decode_9(string):
        res = 0
        m = 1
        for i in range(len(string)-1, -1, -1):
            res += m*int(string[i])
            m *= 9
        return res
    
    def translate_to_nine(string):
        strin = ''
        for i in range(len(string)):
            if int(string[i])>4:
                strin += str(int(string[i])-1)
            else:
                strin += string[i]
        return strin
    
    string = decode_9(translate_to_nine(str(num)))
    
    return string

num = int(input())
print(translate(num)) """

# 29. package transport
""" li = list(int(i) for i in input().split())
max_weight = int(input())

li.sort()
temp = 0
for i in range(min(len(li), 1000)):
    temp += li[i]
    if temp > max_weight:
        p = i
        break
print(p) """

# 30. the length of a continue string
""" string = input()
k = int(input())
string += 'a'
dirs = {}
res = []
temp = ''
for i in range(len(string)):
    if temp == '':
        temp = string[i]
    elif string[i] == temp[-1]:
        temp += string[i]
    else:
        if temp[0] not in res:
            res.append(temp[0])
            dirs[temp[0]] = len(temp)
        elif len(temp)>dirs[temp[0]]:
            dirs[temp[0]] = len(temp)
        temp = string[i]
res.sort(key=lambda x: dirs[x], reverse = True)
# print(res, dirs)
if k>len(res):
    print(-1)
else:
    print(dirs[res[k-1]]) """

# 31. the smallest abs of the sum of two numbers
""" nums = [int(i) for i in input().split()]
res = 65535
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        m = abs(nums[i]+nums[j])
        if m<res:
            res = m
print(res) """

# 32. flowline
""" m, n = (int(i) for i in input().split())
work = [int(i) for i in input().split()]
time = 0
if m >= n:
    time = max(work)
else:
    work.sort()
    workstation = [0 for _ in range(m)]
    for i in range(len(work)):
        min_flow = min(workstation)
        min_location = workstation.index(min_flow)
        workstation[min_location] += work[i]
    time = max(workstation)
print(time) """

# 33. the min of the sum of two numbers with the random orser
""" nums = [int(i) for i in input().split()]
res = (0, 0, 65532)
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if abs(nums[i]+nums[j])<res[2]:
            res = (min(nums[i], nums[j]), max(nums[i], nums[j]), abs(nums[i]+nums[j]))
print(res) """

# 34. the dispatch of the resourse of memory
""" resourse = input().split(',')
request = [int(i) for i in input().split()]
dirs = {}
resourse_li = []
for each in resourse:
    a, b = (int(i) for i in each.split(':'))
    resourse_li.append(a)
    dirs[a] = b
resourse_li.sort()
res = []
for each in request:
    c = 1
    for i in range(len(resourse_li)):
        if resourse_li[i] >= each:
            res.append(True)
            dirs[resourse_li[i]] -= 1
            if dirs[resourse_li[i]] == 0:
                resourse_li.pop(i)
            c = 0
            break
    if c:
        res.append(False)
print(res) """

# 35. check the equation is whether legal and return the most minus
""" def check_input(tec, var, resourse, condition):
    control = 1
    for ind, val in enumerate(tec):
        if len(val) != len(str(float(val))):
            control = 0
        tec[ind] = float(val)
    for ind, val in enumerate(var):
        if len(val) == len(str(float(val))):
            control = 0
        var[ind] = float(val)
    for ind, val in enumerate(resourse):
        if len(val) != len(str(float(val))):
            control = 0
        resourse[ind] = float(val)
    for each in condition:
        if each not in {'>', '>=', '<', '<=', '='}:
            return False
    if control:
        return True
    else:
        return False

tec, var, resourse, condition = (i.split() for i in input().split(';'))
res_bool = check_input(tec, var, resourse, condition)
n = len(var)
res = 0
s = 0
for ind, val in enumerate(tec):
    x = var[ind%n]
    s += val*x
    if ind%5 == 4:
        m = s-resourse[ind//n]
        if m>res:
            res = m
        s = 0
print(res_bool, int(res)) """

# 36. judge the substring of the string
""" target = input()
source = input()
l = len(target)-1
res = -1
for i in range(len(source)-1, -1, -1):
    if source[i] == target[l]:
        l -= 1
    if l == -1:
        res = i
        break
print(res) """

# 37. combine the urls
""" def standard(string):
    if string[-1] == '/':
        string = string[:-1]
    if string[0] != '/':
        string = '/' + string
    return string
a, b = input().split()
print(standard(a)+standard(b)) """

# 38. to arrangr the reasonable party
""" n = int(input())
li = [int(i) for i in input().split()]
target = int(input())
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        if li[i]+li[j] == target:
            res += 1
print(res) """

# 39. find a continue nums order
""" sum_n, n = (int(i) for i in input().split())
step = 1
start = int((sum_n/n)-step*(n-1)/2)
res = [start+i for i in range(n)]
print(res) """

# 40. calculate the smallest of the int in a string
""" string = input()
res = []
resul = []
temp = ''
for val in string:
    if ord(val) >= ord('0') and ord(val) <= ord('9'):
        temp += val
    elif val == '-' and len(temp):
        res.append(temp)
        temp = '-'
    elif val == '-' and not len(temp):
        temp = '-'
    elif len(temp):
        res.append(temp)
        temp = ''
for each in res:
    if each[0]=='-':
        resul.append(int(each))
    else:
        for i in each:
            resul.append(int(i))
print(sum(resul)) """

# 41. the economic company
""" n = int(input())
money = [int(i) for i in input().split()]
target = int(input())
money.sort()
res = 0
for i in range(n-1):
    if money[i]>=target:
        res += 1
    else:
        for j in range(i+1, n):
            if money[i]+money[j]>=target:
                res += 1
                money.pop(j)
                money.append(0)
print(res) """

# 42. delete the letter which showed the min in the string
""" k = input()
string = []
for each in k:
    string.append(each)
key = set(string)
dirs = {}
for each in key:
    dirs[each] = string.count(each)
string.sort(key=lambda x: dirs[x])
con = dirs[string[0]]
res = []
for each in string:
    if dirs[each] != con:
        res.append(each)
if res == []:
    print('empty')
else:
    r = ''
    for each in res:
        r += each
    print(r) """

# 43. the classification of the data
""" def encode_two(num):
    string = str(num%2)
    while num//2:
        num = num//2
        temp = str(num%2)
        string = temp+string 
    return string

def check_value(num, b, c):
    string = encode_two(num)
    print(string)
    num = 0
    for i in string:
        num += int(i)
    if num%b<c:
        return num%b
    else:
        return 0

ref = [int(i) for i in input().split()]
res = 0
for i in range(2, len(ref)):
    print(check_value(ref[i], ref[1], ref[0]))
    res += check_value(ref[i], ref[1], ref[0])
print(res) """

# 44. to describe a order
""" def devide(string):
    res = []
    temp = ''
    for ind, each in enumerate(string):
        if temp == '' or each == temp[-1]:
            temp += each
            if ind == len(string)-1:
                res.append(temp)
        else:
            res.append(temp)
            if ind == len(string)-1:
                res.append(each)
            else:
                temp = each
    return res

def calculate(k):
    if k == 1:
        return '1'
    else:
        li = devide(calculate(k-1))
        string = ''
        for each in li:
            string = string+str(len(each))+each[0]
        return string
while True:
    k = int(input())
    print(calculate(k)) """

# 45. to paint the number
""" nums = [int(i) for i in input().split()]
dirs = {}
for each in nums:
    dirs[each] = 1
res = 0
if 1 not in nums:
    for i in range(len(nums)):
        if dirs[nums[i]]:
            dirs[nums[i]] = 0
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i] == 0:
                    dirs[nums[j]] = 0
            res += 1
else:
    res = 1
print(res) """

# 46. two devide tree
""" def find_root(ind):
    if ind == 2 or ind == 1:
        return [0]
    elif ind%2 == 0:
        return find_root(ind//2-1)+[ind//2-1]
    else:
        return find_root(ind//2)+[ind//2]
nums = [int(i) for i in input().split()]
n = len(nums)
k = -1
ind = 0
while ind<n:
    k += 1
    ind += 2**k

ind = ind - 2**k + 1
temp = []
for i in range(ind,len(nums)):
    if nums[i] != -1:
        temp.append(nums[i])
leaf_value = min(temp)
for i in range(ind, len(nums)):
    if nums[i] == leaf_value:
        leaf = i
        break
path = find_root(leaf)
path.append(leaf)
res = []
for each in path:
    res.append(nums[each])
print(res) """

# 47. combine the order number
""" length = int(input())
n = int(input())
nums = []
for i in range(n):
    nums.append([int(i) for i in input().split()])
control = [1 for _ in range(n)]
res = []
minus = length
while sum(control):
    for i in range(n):
        print(nums, res)
        if control[i] and len(nums[i])>minus:
            res += nums[i][:minus]
            nums[i] = nums[i][minus:]
            minus = length
        elif control[i] and len(nums[i])==minus:
            res += nums[i]
            control[i] = 0
            minus = length
        elif control[i] and len(nums)<minus:
            res += nums[i]
            control[i] = 0
            minus = minus-len(nums[i])
print(res) """

# 48. remove the same value and sort the orser numbers
""" nums = [int(i) for i in input().split()]
dirs = {}
for each in set(nums):
    dirs[each] = nums.count(each)
nums.sort(key=lambda x:dirs[x], reverse = True)
res = list(set(nums))
res.sort(key=lambda x:nums.index(x))
print(res) """

# 49. the smallest number which is consisit by the order numbers
""" def mysort(li):
    for i in range(len(li)):
        for j in range(0, len(li)-i-1):
            if len(li[j])>len(li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]
            elif len(li[j]) == len(li[j+1]):
                for k in range(len(li[j])):
                    if li[j][k] > li[j+1][k]:
                        li[j], li[j+1] = li[j+1], li[j]
                        break
                    if li[j][k] < li[j+1][k]:
                        break

def rearrangesort(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if li[j][0] > li[j+1][0]:
                li[j], li[j+1] = li[j+1], li[j]
            elif li[j][0] == li[j+1][0]:
                p = 0
                while True:
                    p += 1
                    if len(li[j])>p and len(li[j+1])>p:
                        if li[j][0] > li[j+1][0]:
                            li[j], li[j+1] = li[j+1], li[j]
                            break
                        elif li[j][0] < li[j+1][0]:
                            break
                    elif len(li[j])>len(li[j+1]):
                        if li[j][p] > li[j][0]:
                            li[j], li[j+1] = li[j+1], li[j]
                            break
                        else:
                            break
                    elif len(li[j])<len(li[j+1]):
                        if li[j+1][p] < li[j+1][0]:
                            li[j], li[j+1] = li[j+1], li[j]
                            break
                        else:
                            break
                    else:
                        break
    return li

nums = input().split()
mysort(nums)
if len(nums)<=3:
    res = rearrangesort(nums)
else:
    res = rearrangesort(nums[:3])
string = ''
for each in res:
    string += each
print(string) """

# 50. a flower number
""" def isflowernumber(num):
    string = str(num)
    n = len(string)
    res = 0
    for each in string:
        res += int(each)**n
    if res == num:
        return True
    else:
        return False

n, k = (int(i) for i in input().split())
start = 10**(n-1)
end = 10**n
control = -1
res = -1
for i in range(start, end):
    if isflowernumber(i):
        control += 1
        if control == k:
            res = i
            break
print(res) """

# 51. the multiply of several pure number
""" def ispure(num):
    if num == 2:
        return True
    else:
        con = num**0.5
        if con - int(con) == 0:
            return False
        else:
            for i in range(2,int(num)):
                if num%i == 0:
                    return False
            return True

num = int(input())
con = num**0.5
p = 0
if con - int(con) == 0:
    print(int(con), int(con))
else:
    for i in range(2, int(con)+1):
        if num%i == 0 and ispure(i) and ispure(num//i):
            p = 1
            a, b = i, num//i
    if p:
        print(a,b)
    else:
        print(-1,-1) """

# 52. the most area of sun resourse board
""" nums = [int(i) for i in input().split()]
res = 0
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        m = min(nums[i], nums[j])*(j-i)
        if m>res:
            res = m
print(res) """

# 53. stastistics of the cars in parking
""" li = input().replace(' ', '')
port = li.split('0')
res = 0
for each in port:
    m = len(each)
    if m and m%3 == 0:
        res += m//3
    elif m:
        res += m//3+1
print(res) """

# 54. statistic the scores of shoot comprtition
