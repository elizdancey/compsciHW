Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1a
print("Hello, world!")
Hello, world!

#1b
print("Hello", "world!")
Hello world!
#In this example the words print without a comma since it was left outside of quotations

#1c
print(3)
3

#1d
print(3.0)
3.0
#In these examples they print out whatever value is in the parenthesis

#1e
print(2+3)
5

#1f
print(2.0 + 3.0)
5.0

#1g
print("2"+"3")
23
#Examples E and F and very similar while example g printed out the numbers side by side instead of adding them together

#1i
print(2*3)
6

#1j
print(2**3)
8
#In these examples a single "*" multiplies two integers while "**" puts the first integer to the value of the second

#1k
print(7/3)
2.3333333333333335

print(2//3)
0
#if a single "/" is used division is done that displays a decimal remainder. If "//" is used then division is still used but it does not display a remainder

#Chaotic function
n = eval(input("How many numbers should I print?"))
x = eval(input("Enter a number between 0 and 1: "))
SyntaxError: multiple statements found while compiling a single statement
#try number 2
def main():
    n = eval(input("How many numbers should I print?"))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)
main()
SyntaxError: invalid syntax
#I'm not sure what I did wrong

>>> def main()
SyntaxError: expected ':'
>>> def main():
...     n = eval(input("Input the distance in kilometers you would like to convert"))
...     print(n*0.62 "miles")
...     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> def main():
...     n = eval(input("Input the distance in kilometers you would like to convert"))
...     print(n*0.62 "miles");
...     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> #I'm not sure what to do here
>>> 
>>> def main():
...     P = 10000
...     n = 12
...     r = 0.08
...     t = input(input("How many years is the money compounded for?"))
...     A = P(1+(r/n)^nt
... main()
...           
SyntaxError: '(' was never closed
>>> def main():
...     P = 10000
...     n = 12
...     r = 0.08
...     t = input(input("How many years is the money compounded for?"))
...     A = P(1+(r/n))^nt
... main()
SyntaxError: invalid syntax
>>> def Pert():
...     P = 10000
...     n = 12
...     r = 0.08
...     t = input(input("How many years is the money compounded for?"))
...     A = P(1+(r/n))^nt
... Pert()
SyntaxError: invalid syntax
