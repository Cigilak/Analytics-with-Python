##Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
##The numbers obtained should be printed in a comma-separated sequence on a single line.

#Solution:
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)


##Define a class which has 2 methods. Once to get an input of string and the other to print the string in an upper case
class objectString(self):
    def __init__(self):
        self.s = ""             #constructor
    def getString(self):
        self.s = input()        #method

    def upperString(self):
        print(self.s.upper())   #method

strObj = objectString()
strObj.getString()
strObj.printString()
