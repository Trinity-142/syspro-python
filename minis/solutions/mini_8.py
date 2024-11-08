def format_table(benchmarks, algos, results):
    # Sizes
    benchs_width = len(max(benchmarks + ["Benchmarks"], key=len))
    algos_width = len(max(algos, key=len))
    sum_width = benchs_width + algos_width * len(algos) + 11

    # Column headers
    print(f"| {"Benchmarks":<{benchs_width}} |", end="")
    for algo in algos:
        print(f" {algo:<{algos_width}} |", end="")
    print(f"\n|{"-":-^{sum_width}}|")

    # Row headers and entries
    for bench in benchmarks:
        print(f"| {bench:<{benchs_width}} |", end="")
        for result in results[benchmarks.index(bench)]:
            print(f" {result:<{algos_width}} |", end="")
        print()


format_table(["best case", "worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
