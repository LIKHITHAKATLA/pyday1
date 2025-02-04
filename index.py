#printing single number
print(2)    #1
  
#printing multiple numbers
print(2,5)    #2,5

# arthemetic operations without using variables 
print(5+7)        #12
print(9-4)        #5
print(7*7)        #49
print(6/5)        #1.2
print(4**3)       #64

# arthemetic operations using variable

num1 =45
num2 = 23
print( num1 + num2 )   #68
print( num1 - num2 )   #-22
print( num1 * num2 )   #1035
print( num1 / num2 )   #1.9565217391304348
print( num1 // num2 )  # 1

# strings

print("hii")      #hii
str1= "hii frineds" 
print(str1)         #hii frineds
print(type(str1))  #<class 'str'>
print(len(str1))     #11 

# reassinging to the varibale
str1 = "how are you"
print(str1)     #how are you
print(len(str1))     #11

# indexing
# print char Index value consisting 5 
print("indexing")
print(str1[2])   #w
print(str1[-1])    #u

#slicing
#It is denoted by colon(:) is used to prints the sub string

print("Slicing") 
print(str1[0:3]) #how
print(str1[4:6])# ar
print(str1[4:])# are you
print(str1[:7])  #how are
print(str1[:]) #how are you
print(str1[8:20]) #you

print("After Reverse Slicing")
print(str1[-10:-3]) #ow are

print(str1[-2:-9 : -1]) #oy era
print(str1[0 : : 2]) #hwaeyu
print(str1[-2: :-2])  #o r o