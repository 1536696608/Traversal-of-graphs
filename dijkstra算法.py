import heapq
import math
graph = {"A":{"B":5,"C":1},
         "B":{"A":5,"C":2,"D":1},
         "C":{"A":1,"B":2,"D":4,"E":8},
         "D":{"B":1,"C":4,"E":3,"F":6},
         "E":{"C":8,"D":3},
         "F":{"D":6}
}

def init_dis(graph,s):
    dis = {s:0}
    vertex = graph
    for v in vertex:
        if v != s:
            dis[v] = math.inf
    return dis
    
def dijkstra(graph,s):
    queueh = []
    parent = {}
    seen = set()
    heapq.heappush(queueh,(0,s))
    distance = init_dis(graph,s)
    while len(queueh) > 0 :
        item = heapq.heappop(queueh)
        pair = item[1]
        dist = item[0]
        seen.add(pair)
        vertex = graph[pair].keys()
        for w in vertex:
            if w not in seen:
                if dist + graph[pair][w] < distance[w]:
                    distance[w] = dist + graph[pair][w]
                    parent[w] = pair
                    heapq.heappush(queueh,(distance[w],w))
    return parent,distance

def main():
    parents,distance = dijkstra(graph,"A")
    v = "E"
    print(parents)
    print(distance)
        
main()
