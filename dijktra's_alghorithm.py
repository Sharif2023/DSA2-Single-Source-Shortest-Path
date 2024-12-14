import heapq
def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0,source)] #(distance,node)

    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)

        if curr_distance > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight

            #for better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue,(distance,neighbor))

    return distances

def main():
    graph = {
        's': {'u': 10, 'x': 5},
        'u': {'v': 1, 'x': 2},
        'v': {'y': 4},
        'x': {'u': 3,'v':9, 'y': 2},
        'y': {'s': 7, 'v': 6}
    }
    source = 's'
    distances = dijkstra(graph, source)
    print(distances)

if __name__ == '__main__':
    main()