"""
对于图中所有节点对的最短路径问题
"""

V = 4  # 节点数量
INF = float("inf")

def floyd_warshall(graph):
    # 初始化dist[][]，返回最短路径矩阵
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    show_res(dist)

def show_res(dist):
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%5s" % ("INF"), end=" ")
            else:
                print("%5d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()


if __name__=="__main__":
    graph = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0,   1],
            [INF, INF, INF, 0]]
    floyd_warshall(graph)