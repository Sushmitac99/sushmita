print ("hello world")
import math

#print statement/input code that explains to the user what to do
print("I'm a trapezoid calculator! Give me the two base numbers, height, and the two side lengths of the trapezoid and i'll return the area and perimeter of the trapezoid")
base1 = input("base1: ")
base1 = float(base1)
base2 = input("base2: ")
base2 = float(base2)
height = input("height: ")
height = float(height)
side1 = input("side1: ")
side1 = float(side1)
side2 = input("side2: ")
side2 = float(side2)

#STEP 2
# Code that takes the two base numbers and the height and calculates the area of the trapezoid. 
#Code that takes the two base numbers, height, and two side lengths and calculates the perimeter of the trapezoid.
#Store the result in a variable called area and perimeter
area = ((base1+base2)/2) * height
perimeter = base1+base2+side1+side2

#STEP 3
#output code
print("The area of the trapezoid is: " + str(area))
print("The perimeter of the trapezoid is: " + str(perimeter))

