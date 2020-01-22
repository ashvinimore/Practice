# Enter # two# words # String1 and String2 and # return the # sum
# with more weight.If weights are same then return -1. Weight is the sum of ASCII values of the alphabets in the string.

a = 'madam'
b  = 'madam'
# print(ord(a),ord(b))
a = input("a")
b = input("b")

l = [a,b]
sum = 0
for input in l:
    sum1 = sum
    sum = 0
    for i in input :
        i = ord(i)
        sum = sum + int(i)
    if(sum == sum1):
        print("a,b,-1,same",a,b)
    else:
        print('not same')
    # print(sum)

    # for i in input:
    #     for val in i:
    #     sum = sum + int(i)
    # if(sum == sum1):
    #     print("a,b,-1,same",a,b)
    # else:
    #     print('not same')
    # print(sum,sum1)