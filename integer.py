# 0,1,2,3,4,5,6,7,8,9

a=10
b=20
print(a+b)

# Number system

# binary number system --> 0,1
# octal number system --> 0,1,2,3,4,5,6,7
# decimal number system --> 0,1,2,3,4,5,6,7,8,9
# hexa decimal number system --> 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f

# print("a")
print("a",ord("a"))  # ord is a buil in function it return the number representing the uicode of a specified character
                     # it will be converted back by using chr() function 
print('back to character :',chr(97))
print('b',ord('b'))
print(bin(97))
print(bin(ord("a")))

print(type(a))
# create a empty integer using constructor

c=int()     #int() is constructor of integer datatype
print(c)    # output:0 ; it is a literal of interger 0
d=0     # using literal creating a empty integer

# e=09     # it is an error 0 is not exceptable infront of an integer
# print(e)
# creating empty integer using constructor
print('my practice')
num_empty_with_constructor = int()
print(num_empty_with_constructor)
#creating empty interger without using costructor
num_without_constructor=0
print(num_without_constructor)
