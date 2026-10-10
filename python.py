# task 1 
a = int(input("First integer: "))
b = int(input("Second integer: "))
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print("Numbers are equal")

# task 2

a = int(input("Enter the number: "))
if a<0:
    print("Negative")
elif a>0:
    print("Positive")
else:
    print("Zero")

# task 3
a = int(input("Enter the number: "))
if a%2==0:
    print("Even")
else:
    print("Odd")

# task 4

a = int(input("Your score: "))
if 91<a<100:
    print("A")
elif 81<a<90:
    print("B")
elif 71<a<80:
    print("C")
elif 61<a<70:
    print("D")
elif 51<a<60:
    print("E")
else:
    print("F")

# task 5

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a>b>c or a>c>b:
    print(a)
elif c>b>a or c>a>b:
    print(c)
elif b>a>c or b>c>a:
    print(b)

# task 6
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = input("Enter Operation symbol: ")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
elif c=="**":
    print(a**b)
elif c=="//":
    print(a//b)
else:
    print("Invalid Operation")

# task 7

a = int(input("Enter your age: "))
if 0<=a<=12:
    print("Child")
elif 13<=a<=17:
    print("Teenager")
elif 18<=a<=64:
    print("Adult")
elif a>=65:
    print("Senior")
else:
    print("Invalid Age")

# task 8

a = int(input("Total Amount: "))
if 0<a<100:
    print("No discount")
elif 100<=a<=299:
    print("10% discount","Original price:",a,"Final price:",(a-((a*10)/100)))
elif 300<=a<=499:
    print("15% discount","Original price:",a,"Final price:",(a-((a*15)/100)))
elif a>=500:
    print("20% discount", "Original price:",a,"Final price:",(a-((a*20)/100)))
else:
    print("Invalid Amount")

# task 9

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a>b>c:
    print(c,b,a)
elif a>c>b:
    print(b,c,a)
elif b>a>c:
    print(c,a,b)
elif b>c>a:
    print(a,c,b)
elif c>b>a:
    print(a,b,c)
elif c>a>b:
    print(b,a,c)

# task 10

balance = 1000
a = int(input("Enter the amount you want to withdrawal: "))
if a==0 or a<0:
    print("Invalid Amount")
elif a>balance:
    print("Insufficient balance")
else:
    print("Your Withdrawal was done succesfully,","Remaining Balance:",balance - a)
    

# task 11

a = int(input("Enter the amount of kWh you used this month: "))
if 0<a<100:
    print("You used:",a,"kWh of electricity,","Your billing per kWh will be 0,08 Azn,", "Total Bill:",(a*0.08),"Azn")
elif 101<=a<=300:
    print("You used:",a,"kWh of electricity,","Your billing per kWh will be 0,12 Azn,", "Total Bill:",(a*0.12),"Azn")
elif a>300:
    print("You used:",a,"kWh of electricity,","Your billing per kWh will be 0,15 Azn,", "Total Bill:",(a*0.15),"Azn")
else:
    print("Invalid Amount")(

# task 12

fee = 2
a = int(input("Enter your distance: "))
if 0<=a<=5:
    print("Starting fee:",a,"Your distance fee per km will be 0,70 Azn,", "Total fare:",(fee + (a*0.7)))
elif 5<a<=15:
    print("Starting fee:",a,"Your distance fee per km will be 0,60 Azn,", "Total fare:",(fee + (a*0.6)))
elif a>15:
    print("Starting fee:",a,"Your distance fee per km will be 0,50 Azn,", "Total fare:",(fee + (a*0.5)))

# task 13

a = int(input("Enter your age: "))
b = int(input("Enter your salary: "))
c = int(input("Enter your requested loan amount: "))

if a>=18:
    if b>=500:
        if c<=(b*10):
            print("Loan Approved, You meet all the requirements")
        else:
            print("Loan rejected, requested loan is more than 10 times of your salary")
    else:
        print("Loan, rejected, Your salary is smaller than minimum requirements")
else:
    print("Loan rejected, Your age is too small")

# task 14

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b:
                if b == c:
                    print("Equilateral triangle")
                else:
                    print("Isosceles triangle")
            else:
                if a == c:
                    print("Isosceles triangle")
                else:
                    if b == c:
                        print("Isosceles triangle")
                    else:
                        print("Scalene triangle")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")




# task 15

a = int(input("Enter your exam score: "))
b = int(input("Enter your school score: "))
c = int(input("Enter your age: "))

if c<16:
    print("Application rejected")
    
elif 0<a<=700 and 0<b<=100:
    if a<300:
        print("Rejected, Exam score is too low")
    elif 300<=a<=449:
        if b>80:
            print("Accepted, your school score is above 80")
        else:
            print("Rejected, your school score is below 80")
    elif 450<=a<=599:
        print("Accepted, your exam score is eligible")
    elif 600<=a:
        print("Congratulations, you won a scholarship, you are accepted")
