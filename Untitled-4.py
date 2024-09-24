def find_largest_smallest(arr):
    largest = arr[0]
    smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

# Get input from the user for x in input("Enter the array elements separated by spaces: ").split()]

largest, smallest = find_largest_smallest(arr)

print("Largest number:", largest)
print("Smallest number:", smallest)