# Bellman-Ford Algorithm using Dynamic Programming and verify the time complexity

import numpy as np
import time


def bellman_ford(graph, source):
    distance = np.full(len(graph), np.inf)
    distance[source] = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if distance[j] > distance[i] + graph[i][j]:
                distance[j] = distance[i] + graph[i][j]
    return distance


def main():
    graph = np.array([[0, 4, 2, 0, 0, 0],
                      [0, 0, 0, 3, 10, 0],
                      [0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 2, 8],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]])
    start_time = time.time()
    distance = bellman_ford(graph, 0)
    end_time = time.time()
    print("Time complexity of Bellman-Ford Algorithm using Dynamic Programming is : \n", end_time - start_time)
    print("Distance from source to each node is : ", distance)


if __name__ == '__main__':
    main()