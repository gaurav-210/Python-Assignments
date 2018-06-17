# Q.1- Create a function to calculate the area of a circle by taking radius from user.

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))



pi=3.14
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#
# Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this
# function in a program that determines and prints all the perfect numbers between 1 and 1000.
# [An integer number is said to be “perfect number” if its factors, including 1(but not the number
# itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

# method 1

limit = int(input("enter upper limit for perfect number search: "))

n = 1

while n <=limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n, "is a perfect number")
    n = n + 1

# method 2
#
def perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i == 0:
      sum = sum + i
  if sum == n:
    return True
  else:
    return False
for i in range(1,1001):
  if perfect(i):
    print( i)


# Q.3- Print multiplication table of 12 using recursion.

def table(n,i):
  print (n*i)
  i=i+1
  if i<=10:
    table(n,i)
table(12,1)


 # Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(a,b):
  if b == 1:
    return a
  else:
    return a*power(a,b-1)
print (power(6,2))


# Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
c=factorial(n)
l="output"
d={}
d[l]=c
print(d)