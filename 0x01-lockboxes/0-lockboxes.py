#!/usr/bin/python3
"""
lockboxed algorithm
"""


# def canUnlockAll(graph):
#     """
#     this sum everything in the list into set
#     """
#     if not graph or len(graph) == 0:
#         return True  # If there are no lockboxes, consider it as all unlocked

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

def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return True  # If there are no boxes, consider them all unlocked.

    n = len(boxes)
    visited = set([0])  # Start with box 0 as unlocked
    queue = deque([0])  # Queue for BFS, start with box 0

    while queue:
        current_box = queue.popleft()  # Pop the first box from the queue
        
        # Check all keys inside the current box
        for key in boxes[current_box]:
            # If the key unlocks a box that hasn't been unlocked yet
            if key not in visited and key < n:  # Ignore invalid keys (>= n)
                visited.add(key)  # Mark the box as unlocked
                queue.append(key)  # Add it to the queue to explore its keys

    # Return True if we have visited all the boxes, False otherwise
    return len(visited) == n
