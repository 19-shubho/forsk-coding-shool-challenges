"""
class employee:
    def __init__(self):
        print("inside employee constructor")
emp_1=employee()
emp_2=employee()

"""
class Emp:
    def __init__(self,fN,lN,sal,comp):
        self.firstName=fN
        self.lastName=lN
        self.pay=sal
        self.company=comp
        self.mail=fN.lower()+"."+lN.lower()+"@"+comp+".in"


E1=Emp("Abcd","Zxcv",23001,"ADIBAS")
E2=Emp("Qwerty","Zaqwer",32981,"LOKPAD")

print(E1.firstName)
print(E2.mail)

print(E1.lastName)
print(E1.pay)

#Inheritance-Creating Subclasses
#Super class Parent class or Base class
#Sub class Child class or Derived Class

class Developer(Emp):
    pass
d1=Emp("Asdf","Xswe",94585,"SDFGFRE")
d2=Emp("Fdsf","Kjnbf",98908,"ASDVFD")
print(issubclass(Developer,Emp))

print(issubclass(Emp,Developer))

print(d1.mail)

print(isinstance(d1,Developer))
print(isinstance(d1,Emp))

D1=Developer("Asdf","Xswe",945854,"SDFGFRE")
D2=Developer("Fdsf","Kjnbf",989089,"ASDVFD")

print(isinstance(D1,Emp))
print(isinstance(D1,Developer))



#-----------
    
print(help(Developer))
#-----------


class Developer( Emp ) :
    raise_amount = 1.10
    # this will only affect the instances of the Developer class and not Employee class 

dev_1 = Emp ("Sylvester", "Fernandes",50000)

print (dev_1.pay)
dev_1.apply_raise()
print (dev_1.pay) 

dev_2 = Developer ("Sylvester", "Fernandes",50000)
print (dev_2.pay)
dev_2.apply_raise()
print(dev_2.raise_amount)
print (dev_2.pay) 









