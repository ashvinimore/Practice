# Implement pow(A, B) % C.

# In other words, given A, B and C, find (AB)%C.

# Constraints:
#
# 1 ≤ T ≤ 70
#
# 1 ≤ A ≤ 10^5
#
# 1 ≤ B ≤ 10^5
#
# 1 ≤ C ≤ 10^5

# print(10^5)
def exponentiation():
    raiseto = 5
    raiseto = raiseto + 1
    a = 10
    result = 1
    for i in range(1, raiseto):
        result = a * result
    return result


def moduloExponent(a, b, c):
    b = b + 1
    result = 1
    for i in range(1, b):
        result = a * result
    result = result % c
    return result


def mainfunction():
    T = input()
    T = int(T)
    listinput = []
    flag = 0
    if (1 <= T <= 70):
        for val in range(0, T):
            inputs = input()
            inputs = inputs.split()
            listinput.append(inputs)
        for inputs in listinput:
            if (len(inputs) != 3):
                flag = 1
            else:
                A = int(inputs[0])
                B = int(inputs[1])
                C = int(inputs[2])
                if (1 <= A <= exponentiation() and 1 <= B <= exponentiation() and 1 <= C <= exponentiation()):
                    print(moduloExponent(A, B, C))
                else:
                    flag = 1
    if flag == 1:
        return 0


mainfunction()
