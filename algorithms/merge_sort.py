from algorithms import utils
from math import floor


def merge(llist: list, start: int, mid: int, end: int):
    sequence = []
    temp_list = []
    left = llist[start:mid + 1]
    right = llist[mid + 1:end + 1]

    temp_index = 0
    while len(left) and len(right):
        if left[0] < right[0]:
            temp_list.append(left[0])
            left.pop(0)
        else:
            temp_list.append(right[0])
            right.pop(0)

    temp_list = temp_list + left + right
    for i in range(start, end + 1):
        llist[i] = temp_list[i - start]
        spec = utils.SortingSpec(llist[:], [i], "red")
        sequence.append(spec)
    return sequence


def sort(llist: list):
    def inner_sort(llist: list, start: int, end: int):
        if start < end:
            mid = floor((start + end) / 2)
            inner_list = [
                inner_sort(llist, start, mid),
                inner_sort(llist, mid + 1, end),
                merge(llist, start, mid, end)
            ]
            a, b, c = inner_list
            if not a:
                a = []
            if not b:
                b = []
            return a + b + c

    sequence = inner_sort(llist, 0, len(llist) - 1)
    finish = utils.SortingSpec(llist[:], [], "white")
    sequence.append(finish)
    return sequence
