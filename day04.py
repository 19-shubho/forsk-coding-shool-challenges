print('Pick up items for your grocery shopping list:- ')
print('Type "DONE" once you have finished selecting items.')

list=[]
while(True):
    x=input('Add item: ')
   
    if(x=='DONE'):
        break
    
    if(not x):
        print('Invalid input, try again.')
        continue
    
    list.append(x)
     
print('Here is your grocery list:-')
for i in range(1,len(list)):
    print(i,list[i])
    