# First line of input contains number of testcases T. For each testcase there will be three lines. First line of which contains N, size of vector. Second line contains N positive integers seperated by space, and third line contains X, whose frequency is required.
#
# Output Format:
# For each testcase, print the frequency of X.
#
# User Task:
# Your task is to complete the function findFrequency() which should count the frequency of X and return it.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 106
# 1 <= V[i] <= 1016

t = input("enter test cases")

t = int(t)

if( 1 <= t <= 100):
    for T in range(0,t):
        size = input("enter size of vector")
        print(size)
        n = input("enter numbers")
        if(len(n.split()) > int(size)):
            print("enter valid input with size")
        else:
            x = input("enter value of X")
            count = 0
            for val in n:
               if(val == x):
                   count = count + 1
               else:
                   pass
        print(count)
