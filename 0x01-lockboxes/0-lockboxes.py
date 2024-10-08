#!/usr/bin/python3
# """
# lockboxed algorithm
# """


# def canUnlockAll(graph):
#     """
#     this sum everything in the list into set
#     """
#     int_list = []
#     init_set = set()
#     for i in graph:
#         for j in i:
#             int_list.append(j)
#     init_set.update(int_list)
#     init_set.add(0)

#     """
#     using graph to visit connected node
#     """
#     visited = [0]
#     queue = [0]
#     # visited.append(num)
#     # queue.append(num)
#     new_list = []
#     new_set = set()

#     while queue:
#         m = queue.pop(0)
#         new_list.append(m)
#         for i in graph[m]:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)
#     new_set.update(new_list)
#     if new_set == init_set:
#         return True
#     else:
#         return False
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
