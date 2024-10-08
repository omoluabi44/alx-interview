# 
from collections import deque

def canUnlockAll(graph):
    if not graph or len(graph) == 0:
        return True  # If there are no lockboxes, consider it as all unlocked

    n = len(graph)
    visited = set([0])  # Start with room 0 as unlocked
    queue = deque([0])  # Use deque for efficient pop from the left

    while queue:
        current = queue.popleft()  # Get the next room to explore
        for key in graph[current]:
            if key not in visited and key < n:
                visited.add(key)  # Mark the room as unlocked
                queue.append(key)  # Explore the newly unlocked room

    # If we visited all the rooms, return True
    return len(visited) == n
