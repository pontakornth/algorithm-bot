from algorithms import utils


def sort(llist: list):
    sequence = []
    for i in range(len(llist)):
        current_min_index = i
        for j in range(i, len(llist)):
            if llist[j] < llist[current_min_index]:
                current_min_index = j
        spec = utils.SortingSpec(llist[:], [current_min_index, i], "blue")
        sequence.append(spec)
        llist[current_min_index], llist[i] = llist[i], llist[current_min_index]
    spec = utils.SortingSpec(llist[:], [], "blue")
    sequence.append(spec)
    return sequence
