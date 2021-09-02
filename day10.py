import re
PC=[]

K=open('largestcitiest.txt','r')
D=K.readlines()
C=re.compile( '\s[\w\s]+\s+')
 
T=open('datasheet.txt','r')

for i in D:
    R=C.findall(i)[0]
    PC.append(R.strip())


S=open('datasheet.txt','r')
V=S.read()

Dict={}

for item in PC:
    Z='\s'+item+'\s[\d]+\s'
    M=(re.findall(Z,V)[0:3])
    MS=''.join(M)
    
    Dict[item]=re.findall(r'[0-9]+',MS)
print(Dict)