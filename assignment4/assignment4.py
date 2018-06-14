# Q create a truples of different datatypes and find the length of the truples
t=(1,2,3,5)
t1=(1,8,9,7,5,4)
t2=(1,2)
print(len(t))
print(len(t1))
print(len(t2))
m

# Q2 find largest and smallest element of truples
t={1,2,45,89,6,3}
print(max(t))
print(min(t))


#Q3 wap to find the product of all element of tuples
t=(1,2,4,5)
z= t[0]*t[1]*t[2]*t[3]
print(z)


# Q4 create a set from having input from user

x=int(input("Enter any value"))
y=int(input("Enter any value"))
z=int(input("Enter any value"))
k=int(input("Enter any value"))
s1=set([x,y,z,k])
print(s1)

a=int(input("Enter any value"))
b=int(input("Enter any value"))
c=int(input("Enter any value"))
d=int(input("Enter any value"))
s2=set([a,b,c,d])
print(s2)
print (s1-s2)
print(s1&s2)



# Q5 create a dictionary to store marks of 10 student by user input
d={}
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
name=input("Enter your name:")
marks=int(input("Enter your marks :"))
d[name]=marks
print(d)


# Q6 sorting of a given dictionary


values=list(d.values())
print(values)
values.sort()
print(values)





# Q7 count the no of occurance of each letter of MISSISSIPPI  . store count of every letter with letter in a dictionary

l = list("MISSISSIPPI")
print(l)
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['S']=l.count('S')
d['I']=l.count('I')
d['S']=l.count('S')
d['S']=l.count('I')
d['I']=l.count('I')
d['P']=l.count('P')
d['P']=l.count('P')
d['I']=l.count('I')
print(d)