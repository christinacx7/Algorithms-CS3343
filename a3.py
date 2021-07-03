import random
# Algorithms A3 Assignment
# Filename: a3.py
# Class: CSCI 3343 Algorithms
# Professor: Yang
# Code by: Christina Celestino
# 02 March 2021

# Implement the pseudo algorithm of the Find Maximum Subarray problem using a divide
# and conquer approach in finding the contiguous subarray whose values have the largest
# sum. Given the input and output requirements, your implement should follow the 
# pseudocode provided in the textbook/lecture. You can simulate a period of 100 days
# with a randomly generated price ranging from $50 to $120 and calculate daily changes
# in prices from the generated prices. 


# Array for prices
arr = []
for i in range(0, 100):
   x = random.randint(50,120)
   arr.append(x)


# Max Crossing method
def maxCrossing(arr, low, mid, high):
    leftSum = 0
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    rightSum = 0
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return (arr[maxLeft], arr[maxRight], leftSum + rightSum)


# Max Subarray method
def maxSubarray(arr, low, high):
    if high == low:
        return (arr[low])
    
    mid = (low + high)//2
    
    return max(maxSubarray(arr, low, mid), maxSubarray(arr, mid + 1, high),
    maxCrossing(arr, low, mid, high))


# Output
#max_sum = maxSubarray(arr, 0, len(arr)-1)
count = []
for i in range (len (arr)):
    count.append(i+1)

print("{:<}" "{:<}".format("Day", "   | "), end = " ")
for i in count:
    print(str(i).ljust(10), end = "")

print("\n----------------------------------------------------------------------------------------------------------------")
print("{:<}" "{:<}".format("Price", " | "), end = " ")
for p in arr:
    print(str(p).ljust(10), end = "")
