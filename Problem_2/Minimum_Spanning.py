from collections import defaultdict
import heapq
def minimum_spanning(graph, start_node):
    min_spanning_tree = defaultdict(set)
    
    total_cost = 0
    visited = {start_node}
    edges = [(cost, start_node, to)for to, cost in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            min_spanning_tree[frm].add(to)
            total_cost += int(cost)
            print('Path cost from '+str(frm)+' To '+str(to)+' : '+str(cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next)) 
    print("Total cost: ", total_cost)
    return min_spanning_tree