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