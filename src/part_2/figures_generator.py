import matplotlib.pyplot as plt


markers = ["r+", "bx", "g1", "m."]


def plot_times(sizes, names, all_times, title):
    plt.figure()
    for i in range(len(names)):
        plt.plot(sizes, all_times[i], markers[i], label=names[i])
    plt.xlabel("List size n")
    plt.ylabel("Average time of 3 runs with random lists (s)")
    plt.title(title)
    plt.legend()
    plt.show()


def plot_loglog(log_size, names, all_log_times, all_m, all_k, title):
    plt.figure()
    for i in range(len(names)):
        plt.plot(log_size, all_log_times[i], markers[i],
                 label=f"{names[i]} k = {all_k[i]:.3f}")

        fit = []
        for x in log_size:
            fit.append(all_m[i] + all_k[i] * x)

        line_color = markers[i][0]
        plt.plot(log_size, fit, line_color + "-")
    plt.xlabel("log2 of list sizes")
    plt.ylabel("log2 of sorting times")
    plt.title(title)
    plt.legend()
    plt.show()
