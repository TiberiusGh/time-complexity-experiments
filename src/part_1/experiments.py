from list_generator import generate_list
from threesum_algs import threesum_brute, threesum_pointer
from figures_generator import plot_3_runs, plot_average, plot_loglog
import time
import math


pointer_sizes = [1600, 2300, 3000, 3700, 4400,
                 5100, 5800, 6500, 7200, 7900, 8600, 9300, 10000,
                 10500,  11000]

bruteforce_sizes = [250, 295, 340, 385, 430, 475,
                    520, 565, 610, 655, 700, 745, 790, 835, 870]


def fig1_measure(alg, sizes):
    times = []
    for i in sizes:
        lst = generate_list(i)

        start_time = time.perf_counter()
        alg(lst)
        end_time = time.perf_counter()

        times.append(end_time-start_time)

    return times


def lin_reg(x, y):
    n = len(x)

    x_mean = sum(x) / n
    y_mean = sum(y) / n

    numerator = 0
    denominator = 0

    for i in range(n):
        x_diff = x[i] - x_mean
        y_diff = y[i] - y_mean

        numerator += x_diff * y_diff
        denominator += x_diff ** 2

    k = numerator / denominator
    m = y_mean - k * x_mean

    return m, k


def run_experiment(alg, sizes, name):
    run1 = fig1_measure(alg, sizes)
    run2 = fig1_measure(alg, sizes)
    run3 = fig1_measure(alg, sizes)

    # Figure 1
    plot_3_runs(sizes, run1, run2, run3,
                f"Figure 1: {name}, 3 runs")

    avg_times = []

    for i in range(len(sizes)):
        total = run1[i] + run2[i] + run3[i]
        average = total / 3
        avg_times.append(average)

    # Figure 1a
    plot_average(sizes, avg_times,
                 f"Figure 1a: {name}, average of 3 runs")

    log_size = []
    for i in sizes:
        log_size.append(math.log(i))

    log_time = []
    for i in avg_times:
        log_time.append(math.log(i))

    m, k = lin_reg(log_size, log_time)
    print(name, "k =", k)

    # Figure 2b
    fit = []
    for i in log_size:
        y = m + k * i
        fit.append(y)

    plot_loglog(log_size, log_time, fit, k,
                f"Figure 2b: {name} & straight line")


def run_part1_experiments():
    run_experiment(threesum_brute, bruteforce_sizes, "threesum_brute")
    run_experiment(threesum_pointer, pointer_sizes, "threesum_pointer")
