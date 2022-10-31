#1

##Definite loop: Has a known number of iterations
##Indefinite loop: The number of iterations are unknown
##Both have conditions initialized from the beginning
##
##For loop: A loop that's iterations are based off of the object
##While loop: A loop where the iterations are based off of a condition,
##uses boolean logic
##Both have conditions initialized from the beginning
##
##Interactive loop: A loop that repeats a part of the program based on the user input
##Sentinel loop: A loop that stops if a certain value is met
##Both loops can be manipulated by user input
##
##Sentinel loop: A loop that stops if a certain value is met
##End-of-file loop: A loop that reads through lines of a file,
##ends when there is no more lines to read
##Both loops end when a certain value is met



#2

##P    Q    not(P and Q)
##----------------------
##T    T       F
##T    F       F
##F    T       F
##F    F       T
##
##
##P    Q    (not P) and Q
##------------------------
##T    T         F
##T    F         F
##F    T         T
##F    F         F
##
##
##P    Q     (not P) or (not Q)
##-----------------------------
##T    T          F
##T    F          T
##F    T          T
##F    F          T
##
##
##P    Q    R    (P and Q) or R
##------------------------------
##T    T    T           T
##F    T    T           T
##F    F    T           T
##F    F    F           F
##T    F    F           F
##T    T    F           T
##F    T    F           F
##T    F    T           T
##
##
##P    Q    R    (P and R) and (Q or R)
##--------------------------------------
##T    T    T               T
##F    T    T               F
##F    F    T               F
##F    F    F               F
##T    F    F               F
##T    T    F               F
##F    T    F               F
##T    F    T               T



#3

###a
##def main():
##
##    total=0
##    n=1
##    while n <=100:
##        total= total + n
##        n = n + 1
##    print(total)
##
##main()

#c
##def main():
##
##    total = 0
##    n = 0
##    while n != 999:
##        n = int(input("Enter a number: "))
##        total = total + n
##        
##    print(total-999)
##
##main()

#4 !!!!!!!!!!!!!!!!!!!!

##def main():
##    number1 = 0
##    number2 = 1
##    count = 0
##    n = int(input("Enter a value: "))
##    
##    while count < n-1:
##        number = number1 + number2
##        number1 = number2
##        number2 = number
##        count = count + 1
##        
##    print(number ,"is the ", n, "number of the Fibonacci sequence.")
##        
##main()

#5

##def main():
##
##    num = int(input("Enter a number: "))
##    while num > 1:
##    
##        if num%2 == 0:
##            num = num/2
##            print(num)
##
##        elif num%2 != 0:
##            num = (3 * num) +1
##            print(num)
##
##main()
        
        
        


    
    
