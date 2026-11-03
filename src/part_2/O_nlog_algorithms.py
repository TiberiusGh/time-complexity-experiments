
def merge_sort(lst):
    local_lst = lst.copy()

    if len(local_lst) > 1:
        first, last = 0, len(local_lst)
        mid = (first + last) // 2
        left = local_lst[first:mid]
        right = local_lst[mid:last]

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        sorted = merge_sort_sort(sorted_left, sorted_right)

        return sorted
    else:
        return local_lst


def merge_sort_sort(left, right):
    sorted = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted += [left[i]]
            i += 1
        else:
            sorted += [right[j]]
            j += 1
    while i < len(left):
        sorted += [left[i]]
        i += 1
    while j < len(right):
        sorted += [right[j]]
        j += 1
    return sorted


def quick_sort(lst):
    local_lst = lst.copy()

    if len(local_lst) > 1:
        lst_length = len(local_lst)
        pivot = local_lst[lst_length // 2]

        less = []
        equal = []
        greater = []

        for i in local_lst:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)

        sorted_less = quick_sort(less)
        sorted_greater = quick_sort(greater)

        return sorted_less + equal + sorted_greater
    else:
        return local_lst
