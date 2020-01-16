MorseCode = {}
# test_alpha = int(input("Eneter number of morseciode"))
# for i in  range(0,test_alpha):
#     input_key = input("enter alphabet")
#     input_value = input("enter morse code")
#     MorseCode[input_key] = input_value
# print(MorseCode)
#MorseCode Chart
MorseCode = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def encrypt(input):
    output = ''
    for val in input.split(' '):
        output = output + str([k for k,v in MorseCode.items() if v == val][0])
    return(output)
def decrypt(input):
    input = input.upper()
    output = ''
    if len(input) > 1:
        print(*[MorseCode[val] for val in input if val !=''])
    elif  len(input) > 1:
    print(output)
testcases = int(input("enter number of test cases"))
for t in range(0,testcases):
    try:
        raw_choice,raw_input =input("enter choice and valid input").split('')
        if raw_choice == 1:
            encrypt(raw_input)
        elif raw_choice == '2':
            decrypt(raw_input)
    except Exception as e:
        print("enter valid input", e)





# encrypt(input)
# decrypt(input)

