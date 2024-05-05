import heapq

INF = float('inf')  # Infinity value for distances

def add_edge(adj_list, source, destination, weight):
    adj_list[source].append((destination, weight))
    adj_list[destination].append((source, weight))  # For undirected graph

def dijkstra(vertices, adj_list, source):
    distances = [INF] * vertices
    pq = [(0, source)]  # Priority queue with (distance, vertex)

    distances[source] = 0

    while pq:
        dist_u, u = heapq.heappop(pq)

        if dist_u > distances[u]:
            continue

        for v, weight in adj_list[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))

    return distances

if __name__ == "__main__":
    V = 6  # Number of vertices in the graph
    adj_list = [[] for _ in range(V)]  # Adjacency list representation

    # Adding edges and weights to the graph
    add_edge(adj_list, 0, 1, 4)
    add_edge(adj_list, 0, 2, 1)
    add_edge(adj_list, 1, 2, 2)
    add_edge(adj_list, 1, 3, 5)
    add_edge(adj_list, 2, 3, 2)
    add_edge(adj_list, 2, 4, 1)
    add_edge(adj_list, 3, 4, 3)
    add_edge(adj_list, 4, 5, 2)

    src = int(input("Enter the source vertex: "))  # Source node for shortest path calculation

    shortest_distances = dijkstra(V, adj_list, src)

    print("Shortest distances from source vertex", src, "to all other vertices:")
    for i, dist in enumerate(shortest_distances):
        if dist == INF:
            print("Vertex", i, ": INF")
        else:
            print("Vertex", i, ":", dist)