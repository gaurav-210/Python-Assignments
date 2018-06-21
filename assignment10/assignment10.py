#Q.1 inheritance of animal class and acess the base class:
class animal :
    def animal_attribute(self):
        print("Animal")
class tiger(animal) :
    pass
a=tiger()
a.animal_attribute()

#Q.2.WHAT WILL BE THE OUTPUT OF THE FOLLOWING CODE.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
   #output of above code-A B
                        #A B
#Q.3.Create a class cop and update and extend the mission of cop.
class cop:
    
    
    def __init__(self,name,age,work,desigation):
        self.name=name
        self.age=age
        self.work=work
        self.desigation=desigation
         
    def getdisplay(self):
        print(self.name,self.age,self.work,self.desigation)
    def update(self,name,age,work,desigation):
        self.name=name
        self.age=age
        self.work=work
        self.desigation=desigation
        
class mission(cop):

    def add_mission_details(self,msn):
        self.mission = msn
        print("mission is:",self.mission)
c=mission("gaurav chaouhan",19,"investigation","mission impossible")
c.getdisplay()
c.update("ayush",19,"detective","researching something")
c.getdisplay()
c.add_mission_details("success")
#Q.craete a class shape and ....
class shape:
    def __init__(self,length,breadth):
     self.length=length
     self.breadth=breadth
    
    def area(self):
        print("area=",self.length*self.breadth)
class rectangle(shape):
    print("area of rectangle is")

r = rectangle(7,8)
r.area()
class square(shape):
    print("area of square is")
s=square(5,5)
s.area()