m1='This is my first program in my life'
print(m1)
# string slicing
print(m1[0:35]) #here 0 is included but 35 is excluded
print(len(m1))#to know length of string we use len function
print(m1[0:35:2]) #:2 is used to give gap b/w string
print(m1.find('is'))
print(m1.find('program'))
print(m1[:])      #this will automatically print all the characters,sentences
print(m1[0:])    #this will print from 0 index to end
print(m1[:35])   #this will print from 0 to 235
print(m1[::])  #this will print all this sentences without giving any gap (it automatically take 1)
# negative indexing

print(m1[-3:-1])   #here -3 is included but -1 not
print(m1.upper())   #this will make sentences in upper case

print(m1.lower())
print(m1.isalnum())
print(m1.isalpha())

# print(m1.encode())

# check many functions of string on internet
