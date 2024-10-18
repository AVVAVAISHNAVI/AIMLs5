import heapq

class Node:
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic - estimated distance to goal
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    start_node = Node(start, None)
    end_node = Node(end, None)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Check if the goal is reached
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return the reversed path

        # Generate children
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares (up, down, left, right)
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] < 0 or node_position[0] >= len(maze) or node_position[1] < 0 or node_position[1] >= len(maze[0]):
                continue  # Skip out of bounds positions

            if maze[node_position[0]][node_position[1]] != 0:
                continue  # Skip obstacles (non-walkable cells)

            child = Node(node_position, current_node)

            if child.position in closed_list:
                continue

            # Calculate g, h, and f
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Check if child is already in the open list
            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            heapq.heappush(open_list, child)

    return None  # No path found

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(maze, start, end)
if path:
    print(f"Path found: {path}")
else:
    print("No path found")
