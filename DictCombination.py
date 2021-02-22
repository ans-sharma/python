# Write a Python program to create and display all combinations of letters, selecting each letter
# from a different key in a dictionary.

import random,math

dict1 = {'1': 'ans','3': 'arp', '4': 'roh'}
s = list(dict1.values())
# print(s)

# a1 = list()
# for i in s[0]:
#     for j in s[1]:
#         a1.append(str(i) + str(j))
# print(a1)
# a2 = list()
# for i in a1:
#     for j in s[2]:
#         a2.append(str(i) + str(j))
# print(a2)

def wordCombination(list1):
    if len(list1) == 0:
        return 0
        
    temp = [i for i in list1[0]]
    # print(temp)
    # temp=list()
    # print(temp)

    temp2 = list()
    temp3 = list()
    first_count = 1
    count = len(list1)
    while(count!=1):
        for i in temp:
            for j in list1[first_count]:
                temp2.append(str(i) + str(j))
        # print(temp2)
        temp=[i for i in temp2]
        temp2 = list()
        # temp.pop()
        # print(temp)
        # temp = temp2
        # temp2 = temp3
        first_count = first_count +1
        count = count -1
    print(temp)


wordCombination(s)