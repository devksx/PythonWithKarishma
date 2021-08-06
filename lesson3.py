# tuples packing & unpacking

myTuple = ('a', 'b', 'c')

print("change the value c to z: ")

x, y, z = myTuple # unpacking

print("z value", z)

y = 'new value' #reasiign new unpacked value
myTuple = (x, y, z)  #tuple packing
print("my modified tuple is - ", myTuple, "type: ", type(myTuple) )

print('------------------------\n\n')
# dictionary
# bread = {'k1': 'v1', 'k2': 'v2'} #new dictionary
# print(bread, "type: ", type(bread))

myDict = {'x': 12.4, 'y': 22.4, 'z': 99 }
print("get me the related value with x", myDict['x'])
myBasket = {
    'banana': 3,
    'grape': 250,
    'apple': 5
}
#there is no indexing rule in dictionary unlike lists
print("what is the quantity of grapes in my basket", myBasket['grape'])

myBasket['banana'] += 2 # similart to myBasket['banana'] = myBasket['banana] + 2
print("what is the quantity of banana in my basket", myBasket['banana'])

#modify elements in dictionary
print("what are the keys in my dictionary", myBasket.keys(), type(myBasket.keys()))
print("get me values from my dictionary", myBasket.values())
#dictionary insert key value pair
myBasket['strawberry'] = 8
print("get me my dictionary: ", myBasket)

# remove apple from the key
myBasket.pop('apple')
print("get me my dictionary: ", myBasket)

#clear all key value pairs from dictionary
myBasket.clear()
print("get me my dictionary: ", myBasket)

print("get me the value of banana if it is in my basket: ", myBasket.get('banana'))
print("get me the vaue of pear if it is in my Basket", myBasket.get('pear'))




##########################LISTS###############################

#add or remove elements from list
myList = [1, 2 ,3 , 4, 5, 'hh', 7, 9 ]
myVal = myList.pop(1) #removes 5th element, index as argument to pop()
print("get me my list: ", myList)
print("what is the value i removed?", myVal)

myList.append('iiii') #add element at the end of list
print("get me my list: ", myList)

myVal = myList.pop()
print("get me my list: ", myList)
print("what is the value i removed?", myVal)

myList.append('ka')
print("get me my list: ", myList)

#remove
myList.remove('hh') #takes element as an argument
print("get me my list: ", myList)

#insert
myList.insert(3, 'tt')
print("get me my list: ", myList)

#extend the list, it combines a list with another one
myList.extend(['sub 1', 'sub 2 ', 'sub3'])
print("get me my list: ", myList)

#this takes the element as an argument and place it at the end as a list itself
myList.append(['sub 1', 'sub 2 ', 'sub3'])
print("get me my list: ", myList)

#clear list
myList.clear()
print("get me my list: ", myList)

print('---------------------------')



##booleans
myBool = True
myBool = False

#time - 2 - 3.30 pm GST
#next topics - if else conditions, comparison statements, logical expressions