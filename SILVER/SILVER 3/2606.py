# 2606번 : 바이러스

def dfs(graph, v, visited):
    visited[v] = True
    result = [v]
    
    for i in graph[v]:
        if not visited[i]:
            result += dfs(graph, i, visited)
    return result

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
   
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visited = [False] * (N+1)
print(int(len(dfs(graph, 1, visited)))-1)