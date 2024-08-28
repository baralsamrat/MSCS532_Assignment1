#  Insertion Sort Algorithm that sorts in monotonically decreasing order
def insertion_sort_algo(NUM):
    for i in range(1, len(NUM)):
        key = NUM[i]
        j = i - 1
        while j >= 0 and NUM[j] > key:
            NUM[j + 1] = NUM[j]
            j -= 1
        NUM[j + 1] = key

# Example usage
my_list = input("Enter a list of numbers to sort: ").split()
my_list = [int(num) for num in my_list]

insertion_sort_algo(my_list)

# Print in table format
print("Index\tValue")
for i, num in enumerate(my_list):
    print(f"{i}\t{num}")

