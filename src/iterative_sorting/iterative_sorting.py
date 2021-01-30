# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): #looping through range of that the length of the array -1 belongs to.
        cur_index = i#need to set current index to i so that it can compare to check if it is the smallest
        smallest_index = cur_index #sets smallest index number to what it was in cur_inx
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)): #find the next smallest need a nested for loop spaning the length af the array again
            if arr[smallest_index] > arr[j]: #if the smallest index in the array is greater than the numer at poisition j 
                smallest_index = j #then need to reset the smallest index to j


        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] #switch number at positoon[i] and the smallest_index to be arr[smallest_index] before arr[i]

    return arr

result = selection_sort([10, 1, 2, 9, 23, 0, 102, 101, 10, 10, 10])


print("Selection Sort: ",result)



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i -1, i)
                swapped = True

    return arr

arr = [1, 20, 12, 30, 20, 80, 2, 0, 3, 6] 
  
result = bubble_sort(arr) 
  
print ("Bubble Sort: ",result)



''' 
Bubble sort essentially exchanges the elements whereas selection sort performs 
the sorting by selecting the element. 

Bubble sort is the simplest iterative algorithm operates by comparing each item or 
element with the item next to it and swapping them if needed. It compares the first 
and second element of the list and swaps it.


Selection sort has achieved slightly better performance and is efficient than bubble 
sort algorithm. Suppose we want to arrange an array in ascending order then it functions
by finding the largest element and exchanging it with the last element, and repeat the 
following process on the sub-arrays till the whole list is sorted.
'''

'''
Key Differences Between Bubble Sort and Selection Sort

1. In the bubble sort, each element and its adjacent element is compared and swapped if required. 
On the other hand, selection sort works by selecting the element and swapping that particular 
element with the last element. The selected element could be largest or smallest depending on 
the order i.e., ascending or descending.

2. The worst case complexity is same in both the algorithms, i.e., O(n2), but best complexity is different.
Bubble sort takes an order of n time whereas selection sort consumes an order of n2 time.

3. Bubble sort is a stable algorithm, in contrast, selection sort is unstable.

4. Selection sort algorithm is fast and efficient as compared to bubble sort which is very slow and inefficient.


Bubble sort algorithm is considered to be the most simple and inefficient algorithm, but selection sort algorithm 
is efficient as compared to bubble sort. Bubble sort also consumes additional space for storing temporary variable
and needs more swaps.
'''





'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
