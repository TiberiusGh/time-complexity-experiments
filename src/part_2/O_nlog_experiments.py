from O_nlog_algorithms import merge_sort, quick_sort
from experiment_tools import run_comparison

sizes = [50000, 167857, 285714, 403571, 521429,
         639286, 757143, 875000, 992857, 1110714,
         1228571, 1346429, 1464286, 1582143, 1700000]


def run_nlogn_experiments():
    run_comparison([merge_sort, quick_sort],
                   ["merge", "quick"],
                   sizes, "O(n log n) algorithms")
