'[[[]]]'


para = '(})'
idealpara = ['{}','()','[]']
stackpara = []
pendingstack = []

paralist = list(para)

if len(para) % 2 == 0:
    for val in paralist:
        if (len(stackpara) < 1):
            stackpara.append(val)

        else:
            for value in stackpara:
                flag = 0
                for ideal in idealpara:
                    # print(ideal)
                    if (value == ideal[0]):
                        if(val == ideal[1]):
                            stackpara.remove(value)
                            flag = 0
                            break
                    elif(value == ideal[1]):
                        if(val == ideal[0]):
                            stackpara.remove(value)
                            flag = 0
                            break
                    else :
                        flag = 1
                # if flag == 1:
                #     # stackpara.remove(value)
                #     pendingstack.append(value)
    if stackpara:
        print('not balanced')
    else:
        print('balanced')
else:
    print("no balance")








    # print("stackparaval",stackparavalue,stackpara)


