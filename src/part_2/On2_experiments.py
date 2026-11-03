from On2_algorithms import selection_sort, insertion_sort, bubble_sort
from experiment_tools import run_comparison

sizes = [2000, 2800, 3600, 4400, 5200, 6000,
         6800, 7600, 8400, 9200, 10000, 10800, 11600, 12400, 13000]


def run_On2_experiments():
    run_comparison([selection_sort, insertion_sort, bubble_sort],
                   ["selection", "insertion", "bubble"],
                   sizes, "O(n^2) algorithms")
