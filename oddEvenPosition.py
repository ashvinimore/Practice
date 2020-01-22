# Question 1: Enter two numbers N and x. If x is even then print the sum of odd position numbers present in N and if
# x is odd then print the sum of odd position numbers present in N.
# (The question was not written directly like this. It was a long question which had this logic behind)
#
# Test case 1: Input: N= 1250, x=2;
#
# Output: 6
#
# Test Case 2: Input: N=128456, x=7;
#
# Output: 12

t = input("no of test cases")
t = int(t)
for j in range(0,t):
    print(j)
    n,y = input("Enter a two value: ").split('\t')

    y = int(y)
    sum = 0
    for i, val in enumerate(n):
        if(y%2 == 0):
               if(i % 2 == 0):
                   sum = sum + int(n[i])
               else:
                   pass
        else:

            if (i % 2 != 0):
                sum = sum + int(n[i])
            else:
                pass
    print("sum:",sum)