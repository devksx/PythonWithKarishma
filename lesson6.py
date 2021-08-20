li1 = [] #define li1 as a variable of type list
for i in range(10):
    li1.append(i)
print("li1", li1)

#one line expression
li2 = [(x+5) for x in range(3)]

print("li2", li2)

li1 = li2 #assigning li1, reassignment of li1

x = None #defining a variable, iniyializing
x = 0 #initializing

#nested loop importance
#(li10, li20), (li10, li21)
# for i in li1:
#     for j in li2:
#         print(tuple((i,j))) #this will be printed len(li1)*len(li2)
#     print("next element from li1") #this will be printed len(li1)

# print("normal statemnet") #printed 1 time

#break, continue, pass keywords usage
for i in li1:
    #i will write this later
    pass

for i in li1:
    print(i)
    if(i==7):
        break # break out of the loop
    
print("normal statemnet after break") #printed 1 time

for i in li1:
    print(i)
    if(i==5):
        continue #just skip 5 and continue with next element

#functions in python, What is Object-oriented programming

print("what is 5*6", 5*6)

print("what is 6*7", 6*7)

#function with 
def my_multi(x, y):#defining a function, x and y are arguments of the function, this is mandatory
    print("what is {}*{}? Ans.={}".format(x, y, x*y)) #.format string

# my_multi(8,9) #calling a function

for i in range(5):
    my_multi(i, i+1) #i, i+1 as paraments while calling the function

def my_pretty_multi(x=5, y=5): #keep x, y as 0 as defaults, with arguments
    print("what is {}*{}? Ans.={}".format(x, y, x*y)) #.format string

for i in range(5):
    my_pretty_multi() #wit

def my_function(): #function is without arguments
    print("i'm running inside my function")

my_function()

def my_function_with_return(): #function is without arguments and return statement, returnig a string
    return "i'm running inside my function with return"

#assign whatever my_function_eith_return is returning to my_output variable
my_output = my_function_with_return()
my_output = my_output[:7]
# print(my_output)


#Hw - read about OOP, what is OOP and what are classes, objects
#class timings - 7.35 pm to 9.35pm GST
