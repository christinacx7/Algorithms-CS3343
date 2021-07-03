import sys

# Algorithms A4 Assignment
# Filename: a4.py
# Class: CSCI 3343 Algorithms
# Professor: Yang
# Code by: Christina Celestino
# 23 March 2021

# Implement two versions of the pseudo algorithm of the Rod Cutting 
# problem in a programming language you are familiar with and compare the
# effinciency of those in terms of the number of recursive calls made in the
# recurisve top-down implementation and the number of iterations for the 
# recursive bottom-up implementation. Implement should follow the pseudocode
# provided in the textbook/lecture and use a table below as a model for sample
# prices with p_i dollars of revenue for the length i. You may define p_i
# dollars with more lengths.

# algorithm 1
# top-down
def memoizedCutRod(p,n):
    r = []
    for x in range(0, n):
        r.append(x)

    for i in range(0, n):
        r[i] = -1
    return memoizedCutRodAux(p,n,r)


def memoizedCutRodAux(p,n,r):
    if r[n-1] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        i = 1
        for i in range(1, n):
            q = max(q,p[i] + memoizedCutRodAux(p,n-i,r))
    r[n-1] = q
    return q

# algorithm 2
# bottom-up
def extendedBottomUpCutRod(p,n):
    r = []
    s = []
    for x in range(0, n+1):
        r.append(x)
    
    for y in range(1, n+1):
        s.append(y)

    r[0] = 0
    j = 1
    for j in range(0, n+1):
        q = -1
        i = 1
        for i in range(0, j):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j-1] = i
        r[j] = q
    return r and s

choice = 'Y'
c = 0
# a while loop for program output set to run 5 times while the user enters 'Y' or until the user 
# enters 'N' or an invalid character
while c < 5 and choice == 'Y':
    # output
    n = input("Enter the size of the rod: ")
    # make n = 1
    n = int(n)+1
    # there are two rows and n columns
    rows, cols = (2,int(n))
    # a two dimensional array for output where all values are set to 0
    # for the given n size of the array
    output = [[0 for i in range(cols)] for j in range(rows)]

    # set the first two rows in the first column equal to the strings in the table
    output[0][0] = "length i |"
    output[1][0] = "price Pi |"

    # split the output array after the first column in the first row so you can change the other values
    # without affecting the first column
    topList = output[0]
    # split the output array after the first column in the second row so you can change the other values
    # without affecting the first column
    bottomList = output[1]

    # set the values in topList equal to range 1 to n
    for x in range(1, n):
        topList[x] = x
        x += 1

    # an array for price values
    # had to add 0 to p[0] because all other arrays start at [1]
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # match bottomList values to p values for range 1 to n
    for x in range(1, n):
            bottomList[x] = p[x]

    # print the output array
    for x in output[0]:
        sys.stdout.write("{:4}".format(x))
    print("")
    for x in output[1]:
        sys.stdout.write("{:4}".format(x))
    print("")

    # print revenue
    print("Revenue from top-down algorithm: $", (memoizedCutRod(p,n))-1)
    print("Revenue from bottom-up algorithm: ", extendedBottomUpCutRod(p, n))

    # ask the user if they want to enter another length
    print("Would you like to enter another length? ('Y' or 'N')")
    choice = input().upper()
    if choice != 'Y' or choice != 'N':
        print("You entered an invalid choice. Program Ended.")
    c += 1