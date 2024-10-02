#!/usr/bin/python3
"""
pascal triangle
"""
def pascal_triangle(j):
    """
    get row of pascal triangle
    """

    all_list = []
    prev_list = []
    if j <= 0:
        return []

    for _ in range(j):
        if j == 1:
            return [[1]]
        elif j == 2:

            return [[1], [1, 1]]
            # return all_list.append(prev_list.copy)
        else:
            all_list = [[1], [1, 1]]
            for _ in range(j -2):

                new_lis = all_list[-1]
                new = []
                new.append(1)
                for i in range(len(new_lis) - 1):
                    new.append(new_lis[i] + new_lis[i + 1])
                new.append(1)
                all_list.append(new)

    return all_list
    