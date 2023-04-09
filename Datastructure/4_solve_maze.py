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

# use stack to solve
def solve_maze_by_stack(maze, start, end):
    
    def search(maze, stack, end):
        while True:
            m, n = stack[-1][0], stack[-1][1]
            if stack is []:
               print('No aviliable path!')
               return False
            elif stack[-1] == end:
                print('Yep! I find the path!', stack, step='\n')
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

solve_maze_by_stack(maze, (1,1), (8,8))


# use queue to solve
def solve_maze_by_queue(maze, start, end):
     
