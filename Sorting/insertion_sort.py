def main():
    array = [1, 2, 6, 3, 9, 1, 2, 5, 8]

    # Loop over all the elements
    for i in range(len(array)):

        # Store the current index to use to traverse
        # Compare backwards to insert the current element in the right place towards the left
        index = i

        # Loop backwards comparing the current element to all the ones on the left just before
        # To push it to the back or where it belongs till its possible to push it back
        while index > 0 and array[index - 1] > array[index]:

            # If the left side element is bigger then swap the current and the left element
            array[index - 1], array[index] = array[index], array[index - 1]

            # Reduce the left side index to compare it to the next element from the current position
            index -= 1

    # Print the sorted array after looping over all elements of the array
    print(array)


if __name__ == "__main__":
    main()
