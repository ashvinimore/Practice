def getSum(n):
    sum = 0
    n = str(n)
    for i in n:
        sum = sum + int(i)
    # print(sum)
    return sum


n = 100
print(getSum(n))
