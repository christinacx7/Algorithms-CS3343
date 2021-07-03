import random

# Algorithms A2 Assignment
# Filename: a2.py
# Class: CSCI 3343 Algorithms
# Professor: Yang
# Code by: Christina Celestino
# 24 February 2021

# Implement pseudo code algorithm or priority queue, randomly generate 100 ints
# between 0 and 500 each generated number acts as a key to make a max-heap.
# Display the numbers in the array (this represents a max-heap for the priority queue).
# Test the priority queue by extracting max number (key) from the heap.
# Display the numbers in the array again (this time the max number is removed from
# the heap and the remaining 99 numbers will be displayed in a reorganized max-heap).
# Implement should follow the pseudocode provided and use my variables in the implementation.
# Each must be a separate method.


# Parent function
def Parent(i):
    return i//2

# Left function
def Left(i):
    return 2 * i

# Right function
def Right(i):
    return (2 * i) + 1

# Method to heapify array
def maxHeapify(arr, i):
    n = len(arr) # Size of array 
    largest = i # Initialize largest as root 
    l = Left(i)
    r = Right(i)

	# See if left child of root exists and is 
	# greater than root 
    if l < n and arr[l] > arr[i]: 
	    largest = l
    else:
        largest = i
	# See if right child of root exists and is 
	# greater than root 
    if r < n and arr[r] > arr[largest]: 
		largest = r 

	# Change root, if needed 
    if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] # swap 

		# Heapify the root. 
		maxHeapify(arr, largest) 

# Method to extract max key from the array
def heapExtractMax(arr):
    n = len(arr)
    if n < 1:
        print("Error: Heap Underflow")
    max = arr[0]
    arr[0] = arr[n-1]
    arr.pop(n-1)
    maxHeapify(arr, 1)
    return max

# Method to insert key
def heapInsert(arr, key):
    n = len(arr)
    n = n+1
    arr.append(key)
    heapIncreaseKey(arr, n, key)

# Method to increase key
def heapIncreaseKey(arr, n, key):
    n = n-1
    if key < arr[n]:
        print("Error: new key is smaller than current key")
    arr[n] = key
    while n > 0 and arr[Parent(n)] < arr[n]:
        arr[n],arr[Parent(n)] = arr[Parent(n)],arr[n]
        n = Parent(n)
 
# Randomly generate 100 ints between 0 and 500 and add them to an array
arr = []
for i in range(0, 100):
    x = random.randint(0, 500)
    heapInsert(arr,x)

# Display the numbers in the array/heap
print(arr)

# Test priority queue by extracting a max number from the heap
print(" ")
heapExtractMax(arr)
print(arr)
