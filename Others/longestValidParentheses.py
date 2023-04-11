def longestValidParentheses(s: str) -> int:
    dirs = {')': '(', ']': '[', '}': '{'}
    res = [0]
    stack = [(-1, 's')]
    for ind, val in enumerate(s):
        if val in {'(', '[', '{'}:
            stack.append((ind, val))
        elif stack != [] and stack[-1][1] == dirs[val]:
            stack.pop()
        else:
            stack.append((ind, val))
    stack.append((len(s), 's'))
    for i in range(0, len(stack)-1):
        if stack[i+1][0]-stack[i][0]-1:
            res.append(stack[i+1][0]-stack[i][0]-1)

    return max(res)

s = '(()((()))(()()()()()()((((){{)}}{{}]]{{)}}})))))'
k = longestValidParentheses(s)
print(k)