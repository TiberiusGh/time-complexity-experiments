from list_generator import generate_list


def threesum_brute(lst, sum=0):
    threesum_lst = []
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == sum:

                    sorted_elements = sorted((lst[i], lst[j], lst[k]))
                    imutables = tuple(sorted_elements)

                    threesum_lst.append(imutables)

    return list(set(threesum_lst))


def threesum_pointer(lst, sum=0):
    sorted_lst = sorted(lst)
    threesum_lst = []
    n = len(sorted_lst)

    for i in range(n - 2):
        first_num = sorted_lst[i]

        left_pointer = i + 1
        right_pointer = n - 1

        while left_pointer < right_pointer:
            second_num = sorted_lst[left_pointer]
            third_num = sorted_lst[right_pointer]

            total = first_num + second_num + third_num

            if total == sum:
                threesum_lst.append((sorted_lst[i],
                                     sorted_lst[left_pointer],
                                     sorted_lst[right_pointer]))
                left_pointer += 1
                right_pointer -= 1
            elif total < sum:
                left_pointer += 1
            else:
                right_pointer -= 1

    return list(set(threesum_lst))


def run_part1_tests():
    for _ in range(3):
        lst = generate_list(15)
        print("Input:", lst)
        print("Result Brute:  ", sorted(threesum_brute(lst)))
        print("Result Pointer:", sorted(threesum_pointer(lst)))
        print()
