import random
import timeit
import matplotlib.pyplot as plt
from tabulate import tabulate

def merge_sort(arr: list) -> list:
    """Сортування злиттям (Merge Sort)"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Злиття двох відсортованих списків"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(lst: list) -> list:
    """Сортування вставками"""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def compare_algorithms():
    """Порівняння алгоритмів сортування"""
    sizes = [100, 500, 1000, 2000]
    merge_times = []
    insertion_times = []
    timsort_times = []

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        merge_time = timeit.timeit(lambda: merge_sort(arr[:]), number=5)
        insertion_time = timeit.timeit(lambda: insertion_sort(arr[:]), number=5)
        timsort_time = timeit.timeit(lambda: sorted(arr), number=5)

        merge_times.append(merge_time)
        insertion_times.append(insertion_time)
        timsort_times.append(timsort_time)

    # Таблиця результатів
    table_data = []
    for i in range(len(sizes)):
        table_data.append([
            sizes[i],
            f"{merge_times[i]:.6f}",
            f"{insertion_times[i]:.6f}",
            f"{timsort_times[i]:.6f}"
        ])

    headers = ["Розмір масиву", "Merge Sort", "Insertion Sort", "Timsort (sorted)"]
    print(" Час виконання алгоритмів сортування:\n")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Графік результатів
    plt.plot(sizes, merge_times, label="Merge Sort")
    plt.plot(sizes, insertion_times, label="Insertion Sort")
    plt.plot(sizes, timsort_times, label="Timsort (built-in sorted)")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    compare_algorithms()


