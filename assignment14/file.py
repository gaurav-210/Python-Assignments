# 1
# f=open("dictionary.txt","r")
# print(f.name)
# print(f.mode)

# 2
# content = f.read()
# print(content)
# f.close()
# 3
# content = f.read(10)
# print(content)
# f.close()

# 4
# content =  f.read(10)
# print(content,end="#")
#
# content = f.read(10)
# print(content)
#
# f.close()

# 5
# content =f.readline()
# print(content)
# content =f.readline()
# print(content)
# f.close()

# 6
# content =f.readlines()
# print(content)
#
# print(content[1])
# f.close()

# 7
# f = open("dictionary.txt","w")
# f.write("Jai shri ram")
# f.close()

# # 8   use a instead of w to append
# f = open("text3.txt","w")
# f.close()

# 9
#
# with open("dictionary.txt","r") as f:
#     print(f.close)
# print(f.closed)


# 10
# f = open("dictionary.txt","r")
# print(f.tell())
# content = f.read(10)
# print(content)
# print(f.tell())
# f.close()

# 11
# f.seek(10)
# content = f.read(10)
# print(content)
# f.close()


# 12

# import os
# os.rename("text3.txt","karan.txt")

# 13
# os.remove("karan.txt")


# 15

# with open("dictionary.txt","r") as f1:
#     with open("karan.txt","w") as f2:
#         for line in f1:
#             f2.write(line)


# Q.1- Write a Python program to read last n lines of a file
#
# file = open("karan.txt","r",encoding="utf8")
# content = file.readlines()
#
# file.close()
# n = int(input("Enter number of last lines to be read: "))
# print("The last lines are: ")
# while n > 0:
#     print(content[-n])
#     n-=1
#



# Q.2- Write a Python program to count the frequency of words in a file.
#
# from collections import Counter
# def count(fname):
#         with open(fname) as f:
#                 return Counter(f.read().split())
#
# print("Number of words in the file :",count("karan.txt"))

# Q.3- Write a Python program to copy the contents of a file to another file
# with open("dictionary.txt","r",encoding="utf8") as f1:
#     with open("karan.txt","w") as f2:
#         for line in f1:
#             f2.write(line)


# Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
# with open("karan.txt") as fh1, open("dictionary.txt",encoding="utf8") as fh2:
#     for line1, line2 in zip(fh1, fh2):
#         print(line1+line2)



# Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file
import random

with open("karan.txt", "w") as f:
    for i in range(10):
        numbers = str(random.randint(1, 100))
        f.writelines(numbers + '\n')
        print(numbers)

with open("karan.txt") as f1, open("dictionary.txt", "w") as f2:
    numbers = f1.read().split()
    numbers.sort()
    print(numbers)
    for n in numbers:
        f2.write(n)
        f2.write("\n")

