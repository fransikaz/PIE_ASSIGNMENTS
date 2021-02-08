'''
Homework #4 Lists
A function for apending unique elements to a list
'''

myUniqueList = []  # Array of unique values
myLeftOvers = []  # Array of leftover values


def AppendList(Element):
    'Append unique values to myUniqueList array'
    if Element not in myUniqueList:  # check if the element exists in myUniqueList
        myUniqueList.append(Element)  # Append unique values to myUniqueList
    else:
        myLeftOvers.append(Element)


NonUniqueList = [20, 5, 4, "Shark", [7, 9],
                 "shark", [7, 9], [6, 5], 4, 15, 20, 26, 1, 3, 3, 3]  # Array of non-unique elements
for e in NonUniqueList:
    AppendList(e)


print(myUniqueList)  # Print myUniqueList array after appending unique elements
print(myLeftOvers)  # Print myLeftOvers array after appending leftover elements
