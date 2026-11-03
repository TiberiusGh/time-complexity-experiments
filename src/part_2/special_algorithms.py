def bucket_sort(lst):
    local_lst = lst.copy()

    if not local_lst:
        return local_lst

    # 1. Set up empty buckets
    num_buckets = len(local_lst)
    min_val, max_val = min(local_lst), max(local_lst)

    # Handle single unique value edge case
    if min_val == max_val:
        return local_lst

    buckets = [[] for _ in range(num_buckets)]

    # 2. Scatter: place each number into its bucket
    for num in local_lst:
        index = int((num - min_val) / (max_val - min_val + 1) * num_buckets)
        buckets[index].append(num)

    # 3. Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # 4. Gather: concatenate all buckets
    new_arr = []
    for bucket in buckets:
        for num in bucket:
            new_arr.append(num)

    return new_arr


def radix_sort(lst):
    local_lst = lst.copy()
    if not local_lst:
        return local_lst

    # 1. Handle negative numbers by splitting into negative and positive
    negatives = [-x for x in local_lst if x < 0]
    positives = [x for x in local_lst if x >= 0]

    sorted_positives = radix_sort_positive(positives)
    sorted_negatives = radix_sort_positive(negatives)

    # Re-invert negative numbers and reverse their order
    return [-x for x in reversed(sorted_negatives)] + sorted_positives


def radix_sort_positive(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1  # 1 = units, 10 = tens, 100 = hundreds, etc.

    # 2. Sort by each digit (LSD first)
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp):
    # 3. Set up buckets (0-9 for decimal digits)
    buckets = [[] for _ in range(10)]

    # 4. Scatter - place each number in bucket based on current digit
    for num in arr:
        index = (num // exp) % 10
        buckets[index].append(num)

    # 5. Gather - concatenate all buckets sequentially
    new_arr = []
    for bucket in buckets:
        for num in bucket:
            new_arr.append(num)
    return new_arr
