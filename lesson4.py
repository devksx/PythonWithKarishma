
import math
import statistics as st
#arithmatic expressions
x = 6
y = 4
# print('\n', pushes to next line, '\t', adds 4 spaces - tab before a word) 

myNumbers = [1, 2, 3, 4, 4]
print("addition:", x+y, "\nSubtraction:", x-y, "\nMultiplication:",
    x*y, "\ndivision:", x/y,
    "\nfloor function:", x//y, "\nmodulous or remainder",
    x%y, abs(-199),
    "\ncieling function", math.ceil(2.3),
    "\nx^y:", 3**2, "\nx^y:", 5**5, math.sqrt(25),
    "\nsummation of x, y, z:", sum(myNumbers),
    "\nAverage of myNumber:", st.mean(myNumbers),
    "what is the factorial of x:", math.factorial(x)
)

print("----------------------------------------")
#comparison statements
print(x>y, x<y, x==y, x<=y, y<=x, x!=y, x>=y)
#logical expressions
print(x<y and x>0)
print(x==6.0 or x<y)


print("----------------------------------------")
#if else conditions
if(x>10 or y<10):
    print("the given condition True")
else:
    print("the condition given was false")

#nested ifs
if(x<10):
    if(x>5):
        print("my x is less than 10 and it is greater than 5")
    else:
        print("my x is less than 10 and it is not greater than 5")

else:
    print("my x is not less than 10")


name = "Karishma"

if(name=="Karishma"):
    print("Hello Karishma!")
else:
    print("Hello Joseph!")


# good morning
# good afternoon
# good evening

currentTime = 18
#nested if-else
if(currentTime<12):
    print(name, "Good Morning!")

else:
    if(currentTime<17):
        print(name, "Good Afternoon!")
    
    else:
        print(name, "Good evening!")


#if else-if else (elif is else-if)
if(currentTime<12):
    print(name, "Good Morning!")

elif(currentTime<17):
    print(name, "Good Afternoon!")

else:
    print(name, "Good evening!")

#lecture 4 - 7.30 to 9pm GSTm 9/8/21
#control statement
#next lecture loops - for, while, break, continue, pass
