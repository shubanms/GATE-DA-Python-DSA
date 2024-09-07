def main():
    array = [1, 2, 6, 3, 9, 1, 2, 5, 8]

    # Loop over all elements of the array
    for i in range(len(array)):

        # Loop over the same elements except the last element
        # We consider that the right part of the array is sorted
        # We push the largest element to the end of the array
        for j in range(0, len(array)-i-1):

            # We check if the current index element and the element in the next index
            if array[j] > array[j+1]:

                # If the condition is true then we swap the elements essentially pushing the larger element to the next index
                # In the last to the end of the list and then next time we iterate the list we ignore the last index as we know that
                # the end has the largest elements already placed
                array[j], array[j+1] = array[j+1], array[j]

    # Print the sorted array
    print(array)


if __name__ == "__main__":
    main()
