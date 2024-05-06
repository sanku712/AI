import heapq
 

def tree(V, E, edges):

    # Create an adjacency list representation of the graph

    adj = [[] for _ in range(V)]

    # Fill the adjacency list with edges and their weights

    for i in range(E):

        u, v, wt = edges[i]

        adj[u].append((v, wt))

        adj[v].append((u, wt))

    # Create a priority queue to store edges with their weights

    pq = []

    # Create a visited array to keep track of visited vertices

    visited = [False] * V

    # Variable to store the result (sum of edge weights)

    res = 0

    # Start with vertex 0

    heapq.heappush(pq, (0, 0))

    # Perform Prim's algorithm to find the Minimum Spanning Tree

    while pq:

        wt, u = heapq.heappop(pq)

        if visited[u]:

            continue 

            # Skip if the vertex is already visited

        res += wt  

        # Add the edge weight to the result

        visited[u] = True 

        # Mark the vertex as visited

        # Explore the adjacent vertices

        for v, weight in adj[u]:

            if not visited[v]:

                heapq.heappush(pq, (weight, v))  

                # Add the adjacent edge to the priority queue

    return res  

  # Return the sum of edge weights of the Minimum Spanning Tree

if __name__ == "__main__":

    graph = [[0, 1, 5],

             [1, 2, 3],

             [0, 2, 1]]

    # Function call

    print(tree(3, 3, graph))



from sys import maxsize

def selectMinVertex(value, setMST):
    minimum = maxsize
    vertex = 0
    for i in range(len(value)):
        if not setMST[i] and value[i] < minimum:
            vertex = i
            minimum = value[i]
    return vertex
def printMst(parent, graph):
    print("Src.\tDest.\tWeight")
    for i in range(1, len(parent)):
        print(f"{i}\t{parent[i]}\t{graph[i][parent[i]]}")
def findMST(graph):
    V = len(graph)
    parent = [-1] * V
    value = [maxsize] * V
    setMST = [False] * V

    parent[0] = -1
    value[0] = 0

    for i in range(V - 1):
        U = selectMinVertex(value, setMST)
        setMST[U] = True
        for j in range(V):
            if graph[U][j] != 0 and not setMST[j] and graph[U][j] < value[j]:
                value[j] = graph[U][j]
                parent[j] = U

    printMst(parent, graph)

graph = [
    [0, 4, 6, 0, 0, 0],
    [4, 0, 6, 3, 4, 0],
    [6, 6, 0, 1, 8, 0],
    [0, 3, 1, 0, 2, 3],
    [0, 4, 8, 2, 0, 7],
    [0, 0, 0, 3, 7, 0],
]

findMST(graph)
