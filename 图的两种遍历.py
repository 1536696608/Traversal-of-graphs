graph = {"A":["B","C"],
         "B":["A","C","D"],
         "C":["A","B","D","E"],
         "D":["B","C","E","F"],
         "E":["C","D"],
         "F":["D"]
}

def NoSee(i,see):
    if i not in see:
        see.append(i)
        return 1
    return 0
    
def BFS(graph,s):
    queue = []
    parents = {}
    see = []
    see.append(s)
    queue.append(s)
    parents[s] = "null"
    while(len(queue) > 0):
        v = queue.pop(0)
        for i in graph[v]:
            if NoSee(i,see):
                queue.append(i)
                parents[i] = v
        print(v)
    return parents

def DFS(graph,s):
    stack = []
    see2 = []
    see2.append(s)
    stack.append(s)
    while(len(stack) > 0):
        v = stack.pop()
        for i in graph[v]:
            if NoSee(i,see2):
                stack.append(i)
        print(v)

def main():
    parents = BFS(graph,"E")
    #DFS(graph,"A")
    node = 'B'
    while node != "null":
        print(node)
        node = parents[node]
main()
                
