""" 可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 
则不是兄弟单词。现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。
数据范围：1 <= n <= 1000  输入的字符串长度满足 1≤len(str)≤10  ， 1≤k<n 
输入：输入只有一行。 先输入字典中单词的个数n，再输入n个单词作为字典单词。 然后输入一个单词x 最后后输入一个整数k
输出
第一行输出查找到x的兄弟单词的个数m 第二行输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。

样例1：
3 abc bca cab abc 1
输出：2 bca
样例2: 
6 cab ad abcd cba abc bca abc 1
输出：3 bca """

def isBro(str1, str2):
    if set(str1) == set(str2) and str1 != str2:
        return True
    else:
        return False

li = input().split()
n = int(li[0])
data = li[1: n+1]
x = li[n+1]
location = int(li[-1])

res = []
count = 0
for each in data:
    if isBro(x, each):
        res.append(each)
        count += 1
res.sort()

print(count, res[location-1])