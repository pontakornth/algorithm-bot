from algorithms import utils


def sort(llist: list):
    sequence = []
    for i in range(len(llist)):
        key = llist[i]
        prev = i - 1
        while key < llist[prev] and prev >= 0:
            spec = utils.SortingSpec(llist[:], [prev, prev + 1], "yellow")
            sequence.append(spec)
            llist[prev + 1] = llist[prev]
            prev -= 1
        spec = utils.SortingSpec(llist[:], [prev + 1], "yellow")
        llist[prev + 1] = key
        sequence.append(spec)
    spec = utils.SortingSpec(llist[:], [], "white")
    sequence.append(spec)
    return sequence
