# # Q1 Take an input year from user and decide whether it is a leap year or not.
#
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):

     print("The year is a leap year!")

else:

     print("The year isn't a leap year!")

#
# # Q2 Take length and breadth input from user and check whether the dimensions are of square or rectangle.
#

length = int(input("Enter length"))
breadth = int(input("Enter breadth"))
if length == breadth:
    print("Yes, it is square")
else:
    print("No, it is only Rectangle")

# Q3 Take the input age of 3 people and determine oldest and youngest among them.



age1=int(input("Please enter your age"))
age2=int(input("Please enter your age"))
age3=int(input("Please enter your age"))
t=(age1,age2,age3)
print("youngest", min(t))
print("oldest",max(t))



# Q4 Write an if statement that lets a competitor know which of these prizes they won
#  based on the number of points they scored, which is stored in the integer variable
# points(your input). points can only take on positive integer values up to 200.
# If they've won a prize, the message should state "Congratulations! You won a
# [prize name]!" with the prize name. If there's no prize, the message should
# state "Sorry! No prize this time."
#
# Points	Prize
# 1-50	No Prize
# 51-150	Wooden Dog
# 151-180	Book
# # 181-200	Chocolates

#
x = int(input("Enter the points"))
if x<=1 and x<=25:
  print (" sorry! No prize ")
elif x>=51 and x<=150:
  print ("you won a wooden dog !")
elif x>=151 and x<=180:
  print ("You won a Book!")
elif x>=181 and x<=200:
  print("You won a chocolates")
else:
      print ("you won concentration prize")



# Q.5- A shop will give discount of 10% if the cost of purchased
# quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.


quantity = int(input("Enter Quantity:"))
if quantity*100 > 1000:
  print ("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print ("Cost is",quantity*100)
