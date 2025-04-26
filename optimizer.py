from collections import defaultdict
import heapq

def build_graph(routes):
    graph = defaultdict(list)
    for r in routes:
        graph[r['from_node']].append((r['to_node'], r['cost']))
    return graph

def dijkstra(graph, start, end):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        cost, node, path = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == end:
            return cost, path

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path))

    return float('inf'), []
