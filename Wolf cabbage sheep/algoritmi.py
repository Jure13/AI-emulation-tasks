from v2 import Stanje


def generate(state, graphDict):    
    if str(state) in graphDict:
        return 0
    
    print(state)    
    graphDict.add(str(state))
    
    if state.is_solved():
        return graphDict
    
    if state.is_terminal():
        return 0
    
    for i in state.all_actions():
        state.action(i)
        
        generate(state, graphDict)
        
        state.undo_action(i)
    
    return graphDict
    

def solution_dfs(state):
    stack = [state]
    dict = { str(state): None }
    visited = set()
    
    while len(stack) > 0:    
        zadnji = stack.pop(-1)
        
        if zadnji.is_terminal():
            visited.add(zadnji)
            
            if zadnji.is_solved():                
                while zadnji != None:
                    print(zadnji)
                    zadnji = dict[str(zadnji)]
                return dict
            
        elif str(zadnji) not in visited:
            visited.add(zadnji.__str__())
            #visited[str(state)] = zadnji
            
            for i in zadnji.next_states():
                if str(i) not in dict:
                    dict[str(i)] = str(zadnji)
                stack.append(i)
    
    return dict

def solution_bfs(state):
    stack = [state]
    visited = { str(state): None }
    
    while len(stack) > 0:
        stackNext = stack.pop()
        
        if not stackNext.is_terminal():
            for state in stackNext.next_states():
                 if str(state) not in visited:
                     visited[str(state)] = str(stackNext)
                     
                     if state.is_solved():
                         while state:
                             print(state)
                             state = visited[str(state)]
                         return visited
                     stack.append(state)
    
    return visited

def BestFS(state):
    stack = [state]
    visited = { str(state): None }
    
    while len(stack) > 0:
        stackNext = stack.pop()
        
        if not stackNext.is_terminal():
            for state in stackNext.next_states():
                 if str(state) not in visited:
                     visited[str(state)] = str(stackNext)
                     
                     if state.is_solved():
                         while state:
                             print(state)
                             state = visited[str(state)]
                         return visited
                     stack.append(state)

            stack = sorted(stack, key = heuristic)
            
    return visited

def heuristic(state):
    counter = 0
    right = state.State[-4:]
    
    for empty in right:
        if(empty == "-"):
            counter += 1

    return counter



if __name__ == "__main__":
    state = Stanje()
    
    print("Sa \"generate\":\n")
    generate(state, set([]))
    
    print("\n----------\n")
    print("Sa \"BFS\":\n")
    solution_bfs(state)
    
    print("\n----------\n")
    print("Sa \"DFS\":\n")
    solution_dfs(state)
    
    print("\n----------\n")    
    print("Sa \"BestFS\":\n")
    BestFS(state)