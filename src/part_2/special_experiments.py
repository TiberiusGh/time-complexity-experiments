from O_nlog_algorithms import merge_sort, quick_sort
from special_algorithms import bucket_sort, radix_sort
from experiment_tools import run_comparison

sizes = [200000, 414286, 628571, 842857, 1057143,
         1271429, 1485714, 1700000, 1914286, 2128571,
         2342857, 2557143, 2771429, 2985714, 3200000]


def run_special_experiments():
    run_comparison([merge_sort, quick_sort, bucket_sort, radix_sort],
                   ["merge", "quick", "bucket", "radix"],
                   sizes, "special case vs general algorithms")
