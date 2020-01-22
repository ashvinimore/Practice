numbers = [2, 2, 5, 5,5,50, 1]
hashmap = {}

for val in numbers:
    counts = numbers.count(val)
    print(val,counts)
    hashmap[val] = counts
prevkey = hashmap
prevvalue = 0
# print(hashmap[0])\
print(hashmap)
#
# for key,value in hashmap.items():
#     if(prevkey > key and prevvalue < value ):
#        prevkey  = key
#        prevvalue = value