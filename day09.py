"""
Q=open("simpson_phBook.txt",'r')
#read
#readline
#readlines
Q.read()
Q.close()


Q=open("simpson_phBook.txt",'r')
for line in Q:
    print(line)

Q.close()
#^J\w+\s*(Neu)\s*[\d\-]+
"""
import re
Q=open("simpson_phBook.txt",'r')

for line in Q:
    if (re.search(r'^J\w+\s*(Neu)',line)):
        print(line)

Q.close()

