array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

item = 56

# Iterative approach

low, high = 0, len(array) - 1

while low <= high:
    mid = low + (high - low) // 2

    if array[mid] == item:
        print("Found!")
    elif array[mid] > item:
        high = mid - 1
    else:
        low = mid + 1
