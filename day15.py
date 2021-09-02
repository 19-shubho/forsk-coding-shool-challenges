# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:09:53 2021

@author: Asus
"""

class book:
    #create instance method write_bib_entry
    def __init__(self,lt,ft,tl,pl,pub,yr):
        #create instance variables....
        self.authorlast=lt
        self.authorfirst=ft
        self.title=tl
        self.place=pl
        self.publisher=pub
        self.year=yr
    
    #create instance method write_bib_entry
    def write_bib_entry(self):
        return self.authorlast \
               + ', ' + self.authorfirst \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
#create two instances of book class in the name of beauty and pynut        
beauty=book("Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999")
pynut=book("Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003")

print(book.write_bib_entry(beauty))
print(book.write_bib_entry(pynut))
#another method of printing the attributes of instances
print(beauty.write_bib_entry())
print(pynut.write_bib_entry())
#change the value of year for instance beauty to 2021
beauty.year="2021"
#print the new attributes of instance beauty with new year
print(beauty.write_bib_entry())
