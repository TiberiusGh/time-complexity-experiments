import matplotlib.pyplot as plt


def plot_3_runs(sizes, run1, run2, run3, title):
    plt.figure()
    plt.plot(sizes, run1, marker="o", label="Run 1")
    plt.plot(sizes, run2, marker="o", label="Run 2")
    plt.plot(sizes, run3, marker="o", label="Run 3")

    plt.xlabel("List size n")
    plt.ylabel("Time (s)")
    plt.title(title)
    plt.legend()
    plt.show()


def plot_average(sizes, avg_times, title):
    plt.figure()
    plt.plot(sizes, avg_times, marker="o")
    plt.xlabel("List size n")
    plt.ylabel("Average time (s)")
    plt.title(title)
    plt.show()


def plot_loglog(log_size, log_time, fit, k, title):
    plt.figure()
    plt.plot(log_size, log_time, "o", label="Measured")
    plt.plot(log_size, fit, "-", label=f"Fit, k = {k:.2f}")
    plt.xlabel("log(n)")
    plt.ylabel("log(time)")
    plt.title(title)
    plt.legend()
    plt.show()
