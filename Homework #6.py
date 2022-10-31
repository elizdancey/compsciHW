#1

#Exception handling using try/except
#is similar to exception handling usig ordinary decision structures because they both involve manipulating the program based on an outcome.
#They are different because try/except is only utilized based on the outcome of the program as a whole while other decision structures are
#called based on the events that happen within the program itself.

#2

##def main():
##    grade = int(input("Enter your exam score: "))
##
##    if 90<= grade <=100:
##        print("Your grade is an A")
##    elif 80<= grade <=89:
##        print("Your grade is a B")
##
##    elif 70<= grade <=79:
##        print("Your grade is a C")
##
##    elif 60<= grade <=69:
##        print("Your grade is a D")
##
##    elif grade <60:
##        print("You failed :(")
##
##main()


#3

##def main():
##    
##    timeB = int(input("Enter the starting time: "))
##    a = input("Is the AM or PM?: ")
##    timeE = int(input("Enter the ending time: "))
##    b = input("Is the AM or PM?: ")
##
##    pay = 0
##
##    if a == "PM":
##        if timeB != 12:
##            timeB = timeB + 12
##    elif a == "AM":
##        if timeB == 12:
##            timeB = 0
##    
##
##    if b == "PM":
##        if timeE != 12:
##            timeE = timeE + 12
##    elif b == "AM":
##        if timeE == 12:
##            timeE = 0
##    
##
##    for i in range(timeB,timeE):
##        if i < 21:
##            pay = pay + 2.50
##            
##        elif i > 21:
##            pay = pay + 1.75
##           
##        
##
##    print("The final pay is $",pay)
##
##main()


#4

##def main():
##    
##    age = int(input("How old are you?: "))
##    cit = int(input("How many years have you been a citizen?: "))
##
##    if age >= 30 and cit >= 9:
##        print("You can be a  US senator and a US representative ")
##    elif age >= 25 and cit >= 7:
##        print("You can be a US representative")
##    elif age < 25 or cit < 7:
##        print("You cannot be a US representative or a US senator")
##
##main()

#5

##def grades(grade):
##    
##    
##    s="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAA"
##
##    print("\nYour grade is a",s[grade])
##    
##
##
##def main():
##    
##    try:
##        grade = int(input("ENTER YOUR EXAM SCORE: "))
##        grades(grade)
##        
##
##    except ValueError:
##        print("\nOnly enter score using valid integers")
##        grade = int(input("\nENTER YOUR EXAM SCORE: "))
##        grades(grade)
##        
##    except IndexError:
##        print("\nOnly enter score 1-100")
##        grade = int(input("\nENTER YOUR EXAM SCORE: "))
##        grades(grade)
##main()





        
        


    

 

    
    

    
