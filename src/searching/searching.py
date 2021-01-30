def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i 
    return -1   # not found

arr = [468, 390, 416, 269, 827, 48, 77, 293, 722, 515]

target = 77
print(f'Element found at index ' + str(linear_search(arr, target)))
# Write an iterative implementation of Binary Search

#return either the index of the target in the arr or if the target in not in the arr return -1
def binary_search(arr, target):
    # Your code here
    start_index = 0
    end_index = len(arr) -1
    
    while start_index <= end_index:
        #compare the target element to the midpoint
        middle_index = (start_index + end_index)//2
        #if the midpoint element matches the target then we have found it, return the midpoint index
        if arr[middle_index] == target:
            return middle_index
        #determine which way to go, get rid of hald not using
        #reassign either left of right index to the point to the elemnt past midpoint 
        if arr[middle_index] > target:
            end_index = middle_index -1
        else:
            start_index = middle_index + 1
    return -1  # not found

arr = [1, 2, 3, 4, 5, 6]
target = 3

# Function call
result = binary_search(arr, target)
print(f'Element found at index ' + str(result))


'''

A linear search scans one item at a time, without jumping to any item .

The worst case complexity is  O(n), sometimes known an O(n) search
Time taken to search elements keep increasing as the number of elements are increased.


A binary search however, cut down your search to half as soon as you find middle of a sorted list.

The middle element is looked to check if it is greater than or less than the value to be searched.
Accordingly, search is done to either half of the given list

'''