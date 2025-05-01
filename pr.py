# 1. SWAP TWO NUMBER WITHOUT THIRD VARIABLE

a=5
b=6
a,b=b,a
print("a = ",a," b = ",b )

# 2.SWAP TWO NUMBER WITH THIRD VARIABLE

a=8
b=4
c=b
b=a
a=c
print("a = ",a)
print("b = ",b)

# 3. FIND AREA OF REACTANGLE

lenght = int(input("Enter Area :- "))
width = int(input("Enter Area :- "))
print("Area Of Rectangle is :- ",lenght*width)

# 4. FIND THE AREA OF CIRCLE

radius = int(input("Enter a radius :- "))
pi=3.14
print("Area of Circle :- ",pi*radius**2)

# 5. Enter any 5 different Subjects marks at runtime and find out aggregate marks and average? Each subjects out of 100 marks?
total=0
for i in range(1,6):
    i=int(input("enter a marks:- "))
    total =(total + i)/5
print(total)


# 6. Enter any no. of days at runtime and find out how many years, how many months and how many remaining days?
a=int(input("enter a days :- "))
year = a // 365
remain_days = a % 365
month = a // 30
print("total days :",a,"; year :",year,"; month :",month,"; remain_days :",remain_days)

# 7. Enter any no. at runtime and find out Square?
a=int(input("enter the number :- "))
print(a**2)

# 8. Enter any no. at runtime and find out Cube?
a=int(input("enter the number :- "))
print(a**3)

# 9. Check whether a given year is leap or not?
a=int(input("Enter a year :- "))
print("is leap year" if (a % 4==0 and a%100!=0 or a%400==0) else "is not leap year")