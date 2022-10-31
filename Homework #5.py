#Elizabeth Dancey
#Homework #5
import math
from graphics import *

###1
##
##def mac(animal,sound):
##
##    print("Old Macdonald had a farm, Ee-igh, Ee-igh, Oh!")
##    print("And on that farm he had a", animal, "Ee-igh, Ee-igh, Oh!")
##    print("With a", sound,",",sound, "here and a" , sound, ",", sound, "there.")
##    print("Here a", sound,",there a", sound,",everywhere a", sound,",",sound,".")
##    print("Old Macdonald had a farm, Ee-igh, Ee-igh, Oh!")
##
##
##def main():
##    
##    mac("cow","moo")
##    print()
##    mac("chicken","cluck")
##    print()
##    mac("pig","oink")
##    print()
##    mac("horse","niegh")
##    print()
##    mac("dog","bark")
##    
##
##main()


###2
##
##def avg(amount):
##    m=0
##    for i in range(amount):
##        number = int(input("ENTER NUMBER: "))
##        for x in [number]:
##            m = m + x
##    average = float(m/amount)
##
##    print("The average is ", average)
##
##
##def main():
##
##    amount = int(input("How many numbers would you like to average?: "))
##
##    avg(amount)
##
##main()


###3
##
##def slope(dy,dx):
##
##    slope = dy/dx
##    print("The slope is: ",slope)
##
##def length(dy,dx):
##
##    length = math.sqrt((dx**2) + (dy**2))
##    print("The length is: ",length)
##
##def main():
##    win = GraphWin("Window",1000,1000)
##    win.setCoords(0,0,1000,1000)
##    startPoint = win.getMouse()
##    endPoint = win.getMouse()
##
##    line = Line(startPoint,endPoint)
##    line.setOutline("Red")
##
##    x1 = startPoint.getX()
##    y1 = startPoint.getY()
##
##    x2 = endPoint.getX()
##    y2 = endPoint.getY()
##
##    dx = x2-x1
##    dy = y2-y1
##
##    slope(dy,dx)
##
##    length(dy,dx)
##
##    
##
##
##    line.draw(win)
##    win.getMouse()
##    win.close()
##
##main()


###4
##
##def sumList(nums):
##    
##    for i in range(len(nums)):
##        nums[i] = int(nums[i])
##        
##    print("The sum of the list is: ",sum(nums))
##
##def main():
##
##    nums = (input("Enter a list of numbers: ")).split()
##
##    sumList(nums)
##
##main()


#5

def get_some_strings(n):

    final = []
    for i in range(n):

        string = (input("Enter a word: "))
        final.append(string)

    print(final)



def main():

    n = int(input("How many strings would you like to enter?: "))

    get_some_strings(n)

main()

        

        
    
    
    
    

