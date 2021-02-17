import heapq
from collections import defaultdict
import time
from Minimum_Spanning import minimum_spanning


def main():
    file = open("./Undirected_Input/Input4.txt", "r")
    edges = []

    for line in file.readlines():
        edges.append(line.split())

    last = edges[-1]
    first = edges[0]
    vertices = first[0]
    no_of_edges = first[1]
    graph_type = first[2]

    edges.pop(0)

    if len(last) == 1:
        edges.pop()
    di = {}
    for li in edges:
        di.setdefault(li[0], {})[li[1]] = li[2]

    first_node = list(di)[0]
    start_node = first_node[0]
    print('\nSource vertex: ' + str(start_node) + '\n')
    print('Nodes: ' + str(vertices) + '\n')
    print('Edges: ' + str(no_of_edges) + '\n')

    if graph_type == 'D':
        print('Directed Graph\n')
    else:
        print('Undirected graph\n')

    result = dict(minimum_spanning(di, start_node))

    print('Edges of the tree for a Minimum Spanning Tree: ')
    for key in result:
        print('' + str(key) + ' -> ' + str(result[key]))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("***********************\n")
    toc = time.time()
    print("Runtime : %s sec" % (toc - start_time))
