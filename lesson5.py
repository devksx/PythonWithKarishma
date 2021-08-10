#switch case statement in python
vendingMachine = {0: "coke", 1: "dairymilk", 3: "chocolate milk" } #switcher in python

choice = num(input("enter your choice"))
if(choice>0):
  print("your choice was:", vendingMachine.get(choice))
else:
  print("invalid choice")

#loops

#while loop

x = 10
while(x>10):
  print("yes, x is still greater than 10. now at", x)
  x -= 1
 
salaries = [1000, 2000, 30000, 4000, 50000, 5000]

for salary in salaries:
  salary *= 1.25
  print(salary)

print(salaries) #not added 25% increase

for i in range(9):
  print(i)
  
for i in range(3,10):
  print(i)
 
for i in range(3,10, 3):
  print(i)

  
for i in range(len(salaries)):
  salaries[i] *= 1.25
  
print(salaries) #added with 25% increament


print("===================")

#
##
###
####
#####
######

heightOfTriange = int(input("enter height: "))

currentLine = 1
while(currentLine<=heightOfTriange):
    print("#"*currentLine)
    currentLine += 1

currentLine = 1
while(currentLine<=heightOfTriange):
    print("* "*currentLine)
    currentLine += 1

currentLine = 0
while(currentLine<=heightOfTriange):
    print(" "*int((heightOfTriange - currentLine/2)) + "* "*currentLine)
    currentLine += 1
    
    
    
#today 8-9.45 pm GST
#nested for loops and nested while loops
