def selection_sort(lst):
    local_lst = lst.copy()
    lst_length = len(local_lst)

    if lst_length == 0:
        return local_lst

    for i in range(lst_length):
        index_smallest_val = i

        for j in range(i + 1, lst_length):
            if local_lst[j] < local_lst[index_smallest_val]:
                index_smallest_val = j

        local_lst[i], local_lst[index_smallest_val] = (
            local_lst[index_smallest_val], local_lst[i])

    return local_lst


def bubble_sort(lst):
    local_lst = lst.copy()
    lst_length = len(local_lst)

    if lst_length == 0:
        return local_lst

    for i in range(lst_length):
        for j in range(lst_length - (i + 1)):
            if local_lst[j] > local_lst[j + 1]:
                local_lst[j], local_lst[j + 1] = local_lst[j + 1], local_lst[j]

    return local_lst


def insertion_sort(lst):
    local_lst = lst.copy()
    lst_length = len(local_lst)

    if lst_length == 0:
        return local_lst

    for i in range(1, lst_length):
        current = local_lst[i]
        j = i - 1

        while j >= 0:
            if local_lst[j] > current:
                local_lst[j + 1] = local_lst[j]
                j -= 1
            else:
                break

        local_lst[j + 1] = current

    return local_lst
