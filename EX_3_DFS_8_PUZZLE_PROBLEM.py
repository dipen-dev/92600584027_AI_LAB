# Depth First Search For 8 Puzzle Problem
# Enrollment Number : 92600584027
# Name : Ghodasara Dipen

# Gosl State
goal=(1,2,3,
      4,5,6,
      7,8,0)

#Function to print the puzzle
def print_board(state):
    for i in range (0,9,3):
        print(state[i:i+3])
    print()

#General all Possibal moves
def get_neighbors(state):
    neighbors=[]
    zero=state.index(0)
    row,col=divmod(zero,3)

    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in moves:
        new_row=row+dr
        new_col=col+dc

        if 0<=new_row<3 and 0<=new_col<3:
            new_zero=new_row*3+new_col

            new_state=list(state)
            new_state[zero],new_state[new_zero]= new_state[new_zero],new_state[zero]

            neighbors.append(tuple(new_state))
    return neighbors

# DFS Algorithm (Iterative using a Stack)
def dfs(start):
    stack=[(start,[])]
    visited={start}

    while stack:
        state,path=stack.pop()

        
        if state == goal:
            return path+[state]
        neighbors=get_neighbors(state)
   

        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor,path+[state]))
    return None

# starting state
start=(1,2,3,
       4,0,6,
       7,5,8)

# run DFS
solution=dfs(start)

# print solution
if solution:
    print("Solution Found In",len(solution)-1,"moves:\n")

    for step in solution:
        print_board(step)

else:
    print("No Found")
