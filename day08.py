import re
dir(re)
"""
sub
findall
search
match
compile
"""

s='mhv@gmail.com yhtf@yahoo.com cc@outlook.com'
#ABC@gmail.com ABC@yahoo.com ABC@outlook.com

str='98875456e45aexf87ftfr687gihuh@*9'
x=re.findall('^\d{3}',str)
y=re.search('[a-z]{4}',str)
str3='Forsk forsk school'

s = 'aaa@gmail.com bbb@yahoo.com ccc@outlook.com'

#'ABC@gmail.com ABC@yahoo.com ABC@outlook.com'

sub_s = re.sub('[a-z]*@','ABC@',s)



str1 = 'bluepink123abc123xyz456_0'

re.findall('^\d\d\d', str1)



 

str2 = 'Forsk forsk coding School'

m=re.match('forsk', str2) #^
n=re.search('forsk', str2)


re.match('Forsk', str2)
re.search('Forsk', str2)
#search ⇒ find something anywhere in the string and return a match object. 
#match ⇒ find something at the beginning of the string and return a match object

#version 01
str1 = 'kisan andolan forsklabs@gmail.com 1234 yogendra@forsk.in Sylvester Drishaym2 yogendrasingh@qualcomm.com mohanlal ysingh@mango.com covid yogendra@zdrv.com'

re.findall('\w+@\w+\.\w+', str1 )


#version 02
str1 = 'kisan andolan forsklabs@gmail.com 1234 yogendra@forsk.in Sylvester Drishaym2 yogendrasingh@qualcomm.com mohanlal ysingh@mango.com covid yogendra@zdrv.com'

epattern = re.compile(r'\w+@\w+\.\w+')
epattern.findall(str1 )
