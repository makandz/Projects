N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [9999999999 for i in range(N + 1)]
pq = {(0, 1)}
dist[1] = 0

while len(pq) > 0:
    min_node = pq.pop()[1]

    for adj, weight in graph[min_node]:
        if dist[adj] > dist[min_node] + weight:
            dist[adj] = dist[min_node] + weight
            pq.add((dist[adj], adj))

for i in range(1, N + 1):
    if dist[i] == 9999999999:
        print(-1)
    else:
        print(dist[i])