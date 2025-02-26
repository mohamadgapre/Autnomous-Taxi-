import heapq


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            if neighbor == 'coordinates':
                continue

            weight = attributes.get('weight', float('inf'))
            distance = current_distance + weight

            # Only update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node  # Store previous node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct shortest path
    path = []
    current = end
    while current is not start:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()  # Reverse to get correct order

    return path if distances[end] != float('inf') else []  # Return path or empty if unreachable