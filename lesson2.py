myFamily = [1,2,3,4,5, 6, 7]
print(myFamily)

#list slicing
print("get me first 2 values:", myFamily[0:2], myFamily[:2])
print("get me last 3 values:", myFamily[2:len(myFamily)], myFamily[2:], myFamily[-3:])
print("type", type(myFamily))
myFamily[2] = "changed" #benefit of list over tuple
print("after changing", myFamily)


print("---------------------------------------------------")

#tuple
myTuple = ("first element", "2nd element", 3, 4, 5, 6, 7)
print("type of myTuple:", type(myTuple))
print(myTuple[2:4])
#myTuple[2] = "new change" #tuple does not support reassignment
print("after changing tuple")

# can be used as (x, y, z) - point in graph

#next lecture - tuple unpacking, dictionary

#lecture time - 7.30 pm to 8.50 pm GST