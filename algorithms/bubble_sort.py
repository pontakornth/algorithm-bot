from algorithms import utils


def sort(llist: list):
    sequence = []
    for i in range(len(llist)):
        for j in range(i, len(llist)):
            if llist[i] > llist[j]:
                spec = utils.SortingSpec(llist[:], [i, j], "green")
                sequence.append(spec)
                llist[i], llist[j] = llist[j], llist[i]
    sorted_spec = utils.SortingSpec(llist[:], [], "green")
    sequence.append(sorted_spec)
    return sequence
