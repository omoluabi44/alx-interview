#!/usr/bin/python3
"""
lockboxed algorithm
"""


def canUnlockAll(graph):
    """
    this sum everything in the list into set
    """
    if not graph or len(graph) == 0:
        return True  # If there are no lockboxes, consider it as all unlocked

    int_list = []
    init_set = set()
    for i in graph:
        for j in i:
            int_list.append(j)
    init_set.update(int_list)
    init_set.add(0)

    """
    using graph to visit connected node
    """
    visited = [0]
    queue = [0]
    # visited.append(num)
    # queue.append(num)
    new_list = []
    new_set = set()

    while queue:
        m = queue.pop(0)
        new_list.append(m)
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    new_set.update(new_list)
    if new_set == init_set:
        return True
    else:
        return False
