
# Q1  create a list with user defined

x=int(input("enter any no:"))
y=int(input("enter any no:"))
z=int(input("enter any no:"))
l=[x,y,z]
print(l)

# Q2add the following  list to above created list ['google','apple','facebook','microsoft','tesla']

l=[x,y,z]
k=['google','apple','facebook','microsoft','tesla']
print(l.extend(k))
print(l)

# Q3 count no of time and object occur in a list

l=[x,y,z]
print(l.count(1))


# Q4 4 crerte a list with number and sort it in a ascending order

#first method

l=[x,y,z]
l.sort()
print(l)


#second method

l=[x,y,x]
print(l.sort())
print(l)



# # Q5 given are two one- dimensinal array A and B which are sorted in ascending order
# # write a program to merge them into a single sorted array c that Contains every item
# # from array A and B in ascending order list


A=[1,5,6,7]
B=[7,8,9,3]
A.sort()
B.sort()
print(A)
print(B)
print(A.extend(B))
print(A)
C=A
C.sort()
print(C)


# Q 6 implement a stack and queue using list

# stack operations

S = ["Gaurav", "Ayush", "Manisha"]
S.append("Karan")
S.append("Mayank")
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)


# queue operations


queue =(["Manisha", "Gaurav", "Ayush" ,"Rajat"])
print(queue)
queue.append("Tarun")
print(queue)
print(queue.pop())
queue.append("Ram")
print(queue)
print(queue.pop())
print(queue)




# Q6 optional question


li = [1,2,3,4,5,6,7,8,9,99,100]
odd =[i for i in li if i%2 !=0]
even=[i for i in li if i%2 == 0]
print(even)
print(odd)