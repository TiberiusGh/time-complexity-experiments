import random


def generate_list(length):
    lst = []
    min_val, max_val = -10 * length, 10 * length

    for i in range(length):
        random_number = random.randint(min_val, max_val)

        lst.append(random_number)

    return lst
