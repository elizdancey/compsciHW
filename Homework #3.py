from graphics import *
import math
#Program exercise number 3

##def main():
##    
##    hydrogen = int(input("Enter the number of hydrogen atoms: "))
##    oxygen = int(input("Enter the number of oxygen atoms: "))
##    carbon = int(input("Enter the number of carbon atoms: "))
##
##    hydrogen = float(hydrogen * 1.00794)
##    oxygen = float(oxygen * 15.9994)
##    carbon = float(carbon * 12.0107)
##
##    weight = float(hydrogen + oxygen + carbon)
##
##    print("The toal molecular weight of the carbohydrate is", weight, "grams/mole.")
##
##
##main()

#------------------------------------

#Program exercise number 4

##def main():
##
##    time = float(input("Enter the seconds between the lightning flash and thunder: "))
##
##    time = float(time * 1100)
##
##    distance = float(time / 5280)
##
##    print("The lightning strike is ",distance," miles away.")
##main()

#-----------------------------------------

#Program exercise number 13

##def main():
##
##    n = int(input("How many numbers would you like to sum?: "))
##    m = 0
##    for x in range (n):
##        number = int(input("Enter in the number: "))
##
##        for x in [number]:
##            m = m + x
##
##    print(m)
        
##main()

#--------------------------------------------

#Program exercise 14

##def main():
##    n = int(input("How many numbers would you like to average?: "))
##    m = 0
##    for x in range (n):
##        number = int(input("Enter in the number: "))
##
##        for x in [number]:
##            m = m + x
##            
##    average = m/n
##
##    print("The average is ",average)
##
##main()

#--------------------------------------

#Discussion probelm number 2


#a+b
##def main():
##
##   win = GraphWin("Window",500,500)
##   win.setBackground(color_rgb(0,0,0))
##   pt = Point(130,130)
##   cir = Circle(pt, 50)
##   cir.setFill("blue")
##   cir.setOutline("red")
##   cir.draw(win)
##                     
##   win.getMouse()
##   win.close()
##   
##main()

#c
##def main():
##
##   win = GraphWin("Window",500,500)
##   win.setBackground(color_rgb(0,0,0))
##   pt1 = Point(20,20)
##   pt2 = Point(40,40)
##   r = Rectangle(pt1,pt2)
##   r.setFill(color_rgb(0,255,150))
##   r.setWidth(3)
##  
##   r.draw(win)
##                     
##   win.getMouse()
##   win.close()
##   
##main()

#d
##def main():
##
##   win = GraphWin("Window",500,500)
##   win.setBackground(color_rgb(0,0,0))
##   pt1 = Point(100,100)
##   pt2 = Point(100,200)
##   l = Line(pt1,pt2)
##   l.setOutline("red4")
##   l.setArrow("first")
##  
##   l.draw(win)
##                     
##   win.getMouse()
##   win.close()
##
##main()

#e
##def main():
##
##   win = GraphWin("Window",500,500)
##   win.setBackground(color_rgb(0,0,0))
##   o = Oval(Point(50,50), Point(60,100))
##  
##   o.draw(win)
##                     
##   win.getMouse()
##   win.close()
##
##main()

#f
def main():

    win = GraphWin("Window",500,500)
    win.setBackground(color_rgb(0,0,0))
    pt1 = Point(5,5)
    pt2 = Point(10,10)
    pt3 = Point(5,10)
    pt4 = Point(10,5)
    shape = Polygon(pt1, pt2, pt3, pt4)
    shape.setFill("orange")

    shape.draw(win)
                    
    win.getMouse()
    win.close()
main()

#g
##def main():
##
##   win = GraphWin("Window",500,500)
##   win.setBackground(color_rgb(0,0,0))
##   t = Text(Point(100,100), "Hello World!")
##   t.setFace("courier")
##   t.setSize(16)
##   t.setStyle("italic")
##  
##  
##   t.draw(win)
##                     
##   win.getMouse()
##   win.close()
##
##main()

#------------------------

#Discussion problem number 3

##def main():
##   win = GraphWin()
##   shape = Circle(Point(50,50),20)
##   shape.setOutline("red")
##   shape.setFill("red")
##   shape.draw(win)
##   for i in range(10):
##      p = win.getMouse()
##      c = shape.getCenter()
##      dx = p.getX() - c.getX()
##      dy = p.getY() - c.getY()
##      shape.move(dx,dy)
##   win.close()
##main()
#red circle appears in left hand corner

#-------------------------------

#Programming exercise number 2

##def main():
##
##   win = GraphWin("Window",1000,1000)
##   win.setBackground(color_rgb(0,0,0))
##   pt = Point(500,500)
##  
##   c1 = Circle(pt,500)
##   c1.setFill("white")
##   c2 = Circle(pt,400)
##   c2.setFill("black")
##   c3 = Circle(pt,300)
##   c3.setFill("blue")
##   c4 = Circle(pt,200)
##   c4.setFill("red")
##   c5 = Circle(pt,100)
##   c5.setFill("yellow")
##   
##   
##  
##   c1.draw(win)
##   c2.draw(win)
##   c3.draw(win)
##   c4.draw(win)
##   c5.draw(win)
##                     
##   win.getMouse()
##   win.close()
##
##main()

#--------------------------

##def main():
##
##   win = GraphWin("Window",500,500)
##   win.setBackground(color_rgb(0,0,0))
##   pt = Point(250,250)
##   fac = Circle(pt, 250)
##   fac.setFill(color_rgb(255,175,125))
##
##   pq = Point(345,175)
##   eye1 = Circle(pq,60)
##   eye1.setFill("White")
##
##   pw = Point(155,175)
##   eye2 = Circle(pw,60)
##   eye2.setFill("White")
##
##   pqq = Point(155,200)
##   pupil1 = Circle(pqq,30)
##   pupil1.setFill("Black")
##
##   pww = Point(345,200)
##   pupil2 = Circle(pww,30)
##   pupil2.setFill("Black")
##
##   sm = Point(250,350)
##   smile = Circle(sm,110)
##   smile.setFill("Red2")
##  
##  
##   fac.draw(win)
##   eye1.draw(win)
##   eye2.draw(win)
##   pupil1.draw(win)
##   pupil2.draw(win)
##   smile.draw(win)
##                     
##   win.getMouse()
##   win.close()
##   
##main()

#------------------------------

#Programming exercise 8

##def main():
##   win = GraphWin("Window",500,500)
##   win.setCoords(0,0,500,500)
##   startPoint = win.getMouse()
##   endPoint = win.getMouse()
##
##   l = Line(startPoint,endPoint)
##   l.setOutline("Cyan")
##
##   x1 = startPoint.getX()
##   y1 = startPoint.getY()
##
##   x2 = endPoint.getX()
##   y2 = endPoint.getY()
##
##   dx = x2-x1
##   dy = y2-y1
##
##   slope = dy/dx
##
##   length = math.sqrt((dx**2) + (dy**2))
##
##   print("Length: ",length," Slope: ",slope)
##
##   
##   l.draw(win)
##   win.getMouse()
##   win.close()
##
##
##main()








