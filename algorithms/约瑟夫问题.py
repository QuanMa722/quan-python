
# -*- coding: utf-8 -*-


import timeit


def josephus_solution_one(m: int, n: int) -> list:

    people_list = list(range(1, m + 1))
    index_int = 0
    result_list = []

    while len(people_list) > 0:
        index_int = (index_int + n - 1) % len(people_list)
        result_list.append(people_list.pop(index_int))

    return result_list


def josephus_solution_two(m: int, n: int) -> int:

    index_int = 0

    for index in range(2, m + 1):
        index_int = (index_int + n) % index

    return index_int + 1


def josephus_solution_three(n: int, m: int) -> int:

    if n == 1:
        return 1
    else:
        return (josephus_solution_three(n - 1, m) + m - 1) % n + 1


if __name__ == '__main__':

    m = 41
    n = 3

    result_one = josephus_solution_one(m, n)
    result_two = josephus_solution_two(m, n)
    result_three = josephus_solution_three(m, n)

    print(result_one, result_two, result_three)

    # 时间测试
    people_test = 900
    index_test = 3

    time_one = timeit.timeit(lambda: josephus_solution_one(people_test, index_test), number=1)
    time_two = timeit.timeit(lambda: josephus_solution_two(people_test, index_test), number=1)
    time_three = timeit.timeit(lambda: josephus_solution_three(people_test, index_test), number=1)

    print("Time taken for josephus_solution_one:", time_one, "seconds")
    print("Time taken for josephus_solution_two:", time_two, "seconds")
    print("Time taken for josephus_solution_three:", time_three, "seconds")





