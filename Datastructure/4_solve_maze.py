import copy

maze = [
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
     [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

maze1 = copy.deepcopy(maze)
maze2 = copy.deepcopy(maze)

# use stack to solve
def solve_maze_by_stack(maze, start, end):
    
    def search(maze, stack, end):
        while True:
            m, n = stack[-1][0], stack[-1][1]
            if stack is []:
               print('No aviliable path!')
               return False
            elif stack[-1] == end:
                print('Yep! I find the path!', stack, sep='\n')
                return True
            elif maze[m-1][n] == 0:
                stack.append((m-1, n))
                maze[m-1][n]=1
            elif maze[m][n-1] == 0:
                stack.append((m, n-1))
                maze[m][n-1]=1
            elif maze[m+1][n] == 0:
                stack.append((m+1, n))
                maze[m+1][n]=1
            elif maze[m][n+1] == 0:
                stack.append((m, n+1))
                maze[m][n+1]=1
            else:
                stack.pop()

    stack = []
    stack.append(start)
    maze[start[0]][start[1]]=1
    search(maze, stack, end)

solve_maze_by_stack(maze1, (1,1), (8,8))

from collections import deque
# use queue to solve
def solve_maze_by_queue(maze, start, end):
    dirs = [
        lambda x :(x[0]+1, x[1]),
        lambda x :(x[0], x[1]+1),
        lambda x :(x[0]-1, x[1]),
        lambda x :(x[0], x[1]-1)
     ]
    memo = {}
    memo[start]=0
    q = deque()
    q.append(start)
    maze[start[0]][start[1]]=2
    while True:
        temp = q.popleft()
        if temp == end:
            break
        for dir in dirs:
            if maze[dir(temp)[0]][dir(temp)[1]] == 0:
                q.append((dir(temp)))
                memo[dir(temp)] = temp
                maze[dir(temp)[0]][dir(temp)[1]] = 2
    path = deque()
    path.append(end)
    s = end
    while memo[s]:
        k = memo[s]
        path.appendleft(k)
        s = k
    return path

path = solve_maze_by_queue(maze2, (1, 1), (8, 8))
for i in range(len(path)):
    print(path.popleft())