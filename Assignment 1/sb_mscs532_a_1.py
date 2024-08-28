# Insertion Sort Algorithm that sorts in monotonically decreasing order


def insertion_sort_algo(NUM):
    """
    This function implements the insertion sort algorithm to sort a list of numbers in monotonically decreasing order.

    Parameters:
    NUM (list): The list of numbers to be sorted

    Returns:
    None. The function sorts the list in-place.
    """
    for i in range(1, len(NUM)):
        key = NUM[i]
        j = i - 1
        while j >= 0 and NUM[j] > key:
            NUM[j + 1] = NUM[j]
            j -= 1
        NUM[j + 1] = key

# Test function
my_list = [5, 1, 2, 1, 4]
print("Original list:", my_list)
insertion_sort_algo(my_list)
print("Sorted list:", my_list)


# Get the list of numbers from the user
my_list = input("Enter a list of numbers to sort: ").split()
my_list = [int(num) for num in my_list]

insertion_sort_algo(my_list)

# Print in table format
print("Index\tValue")
for i, num in enumerate(my_list):
    print(f"{i}\t{num}")

