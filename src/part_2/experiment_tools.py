from figures_generator import plot_times, plot_loglog
from list_generator import generate_list
import time
import math


def fig1_measure(alg, sizes):
    times = []
    for n in sizes:
        lst = generate_list(n)

        start_time = time.perf_counter()
        alg(lst)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    return times


def average_of_3_runs(alg, sizes):
    run1 = fig1_measure(alg, sizes)
    run2 = fig1_measure(alg, sizes)
    run3 = fig1_measure(alg, sizes)

    avg_times = []
    for i in range(len(sizes)):
        total = run1[i] + run2[i] + run3[i]
        avg_times.append(total / 3)

    return avg_times


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


def to_log2(values):
    log_values = []
    for value in values:
        log_values.append(math.log2(value))

    return log_values


def run_comparison(algs, names, sizes, title):
    all_times = []
    for alg in algs:
        all_times.append(average_of_3_runs(alg, sizes))

    plot_times(sizes, names, all_times, f"Running times for {title}")

    log_size = to_log2(sizes)

    all_log_times = []
    all_m = []
    all_k = []
    for times in all_times:
        log_times = to_log2(times)
        m, k = lin_reg(log_size, log_times)
        all_log_times.append(log_times)
        all_m.append(m)
        all_k.append(k)

    plot_loglog(log_size, names, all_log_times, all_m, all_k,
                f"Log-log plots for {title}")
