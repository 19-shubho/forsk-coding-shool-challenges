import math
ad=[]
while(True):
    x=input("Enter a Number: ")
    if(not x):
        print('Invalid entry try again.')
        continue
    
    if(x.isdigit()):
        x=int(x) 
        print("Square root of your integer value is: ",math.sqrt(x))
        ad.append(math.sqrt(x))
    elif(x=='break'):
        break
    else:
        print("Length of your string input is: ",len(x))
        ad.append(len(x))
        
print("The list of values are: ",ad)