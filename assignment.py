#W.A.P TO CONCATENATE TWO LIST A=[1,2,3,4]  AND B=[5,6,7,8]
list_a=[1,2,3,4]
list_b=[5,6,7,8]
print(list_a+list_b)
list_a.extend(list_b)
print(list_a)

# W.A.P TO SLICE FROM A LIST [1,'krishna',10.0,0j]  [3:5]
list_slice=[1,'krishna',10.0,0j]
print(list_slice[3:5])
#W.A.P TO CONVERT A STRING  'ABCDEFGHIJKLMNOPQRSTUVWXYZ' INTO  'abcdefghijklmnopqrstuvwxyz' by using method
str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(str.lower())
print(str.casefold())
#W.A.P TO CONVERT A STRING a = "NnkriSHna714@gmail.com" INTO LOWERCASE WITHOUT USING LOWER() METHOD
a="NnkriSHna714@gmail.com"
print(a.casefold())
#W.A.P TO REMOVE SPACES GIVEN IN A STRING 
# a = "     nnkrishna714@gmail.com     " 
a = "     nnkrishna714@gmail.com     " 
print(a)
b=a.strip()
print(b)
#W.A.P TO GET RESULT OF THE FOLLOWING
#c="krishna"
#d="kumar"
#result="krishnakumar" by 3 method
c="krishna"
d="kumar"
print(" ".join([c,d]))
print()
print('{}{}'.format(c,d))
print(f'{c}{d}')
print("first method to concatenate string")
result=c+d
print(result)
print()
print("second method to concatenate string:")
result="%s%s" %(c,d)
print(result)
print()
print("third method to concatenate string:")
result=f'{c}{d}'
print(result)
#W.A.P TO GET 
#c= "krishna"  d= "   kumar"  result = "krishnakumar"
c= "krishna" 
d= "   kumar"  
result=c+d.strip()
print(result)
