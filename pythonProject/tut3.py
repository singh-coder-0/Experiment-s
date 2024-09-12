#typecatinng ,datatype,variable

"""
str():-anything within quotations(' '),(" ")
float():-no. with decimal and without quotations
int():-no. without decimals without quotations
bool() true/false
"""
a=85
b='unknown'
c=85.21

print(type(a))
print(type(b))
print(type(c))

#taking input from users
'''
to take input we use input()
'''
print('Enter a no')
inpnum=input()
print(inpnum)

#typecasting

m=16
n='10'
p=21.0
print(int(float(m)+int(n)+int(p)))


#make calculator using python programming

x=input('Enter a number')

y=input('enter second no')

print(int(x)+int(y))
print(int(x)-int(y))
print(int(x)*int(y))
print(int(int(x)/int(y)))

