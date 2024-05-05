import heapq

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    mst = []
    edge_count = 0

    for edge in edges:
        if edge_count == n - 1:
            break
        u, v, w = edge
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            mst.append(edge)
            union(parent, rank, x, y)
            edge_count += 1

    return mst

if __name__ == "__main__":
    n = 6
    edges = [
        (0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 0, 4), (2, 0, 4), (2, 1, 2),
        (2, 3, 3), (2, 5, 2), (2, 4, 4), (3, 2, 3), (4, 2, 4), (5, 2, 2)
    ]

    mst = kruskal_mst(edges, n)

    print("Edges of the minimum spanning tree:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")