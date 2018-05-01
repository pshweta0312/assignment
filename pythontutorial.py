#ques1#
'''l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))'''


#ques2#
'''def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input())
print (fact(x))'''


#ques3#
'''number = int(input())
dictionary= dict()
for i in range(1,number+1):
    dictionary[i]=i*i

print (dictionary)'''



#ques4#

'''values = input()
l= values.split(",")
t=tuple(l)
print (l)
print(t)'''

#ques5#
'''class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()'''



#ques6#
'''import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))'''


#ques7#
'''input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)'''


#ques8#
'''items=[x for x in input().split(',')]
items.sort()
print (','.join(items))'''


#ques9#
'''lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print (sentence)'''


#ques10#
'''s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))'''


#ques11#
'''value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))'''


#ques12#


'''values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (",".join(values))'''

#ques13#

'''s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])'''



#ques14#

'''s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])'''


#ques15#
'''a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)'''


#ques16#
'''values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))'''


#ques17#

import sys
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(input(values[1]))
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print (netAmount)











    




