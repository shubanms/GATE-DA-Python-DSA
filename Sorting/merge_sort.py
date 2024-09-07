def merge(array, low, mid, high):
    pass


def merge_sort(array, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        # merge(array, low, mid, high)
        print(array[low:high+1])


def main():
    array = [1, 2, 6, 3, 9, 1, 2, 5, 8]

    merge_sort(array, 0, len(array))


if __name__ == "__main__":
    main()
