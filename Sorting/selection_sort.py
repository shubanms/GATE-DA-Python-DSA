def main():
    array = [1, 2, 6, 3, 9, 1, 2, 5, 8]

    # Loop over each element in the array
    for i in range(len(array)-1):

        # Store the current index where the minimum element in the array is present
        # We consider that the left side of the array denoted by the i index is sorted
        min_index = i

        # Loop over the remaining elements in the array
        for j in range(i+1, len(array)):

            # Using the min element index compare it with the current element
            if array[min_index] > array[j]:

                # If the condition is true then update the min index of the smallest element found in the rest of the array
                min_index = j

        # Finally swap the elements that makes the left side of the array sorted on its own
        # Then we move the index one point forward int he next iteration
        array[i], array[min_index] = array[min_index], array[i]

    # Print the sorted array after looping over all elements of the array
    print(array)


if __name__ == "__main__":
    main()
