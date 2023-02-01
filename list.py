#list constructor is list()
#list literal is []
#list is a set of sequence of element(s) 
#list is mutable
# list support slicing 
# list support indexing 
# In python list assume like array but it is not an array.
#list support concatination.

a=list()
print(a)

b=[]
print(a)

#indexing
c=[1,"kalraj",10.0,complex(),4+2j]
print(c)

print(c[1])
print(c[3])

#slicing
print(c[1:4])   #['kalraj', 10.0, 0j]
print(c[::])    #[1, 'kalraj', 10.0, 0j, (4+2j)]
print(c[:])     #[1, 'kalraj', 10.0, 0j, (4+2j)]
print(c[0:])    #[1, 'kalraj', 10.0, 0j, (4+2j)]
print(c[::1])   #[1, 'kalraj', 10.0, 0j, (4+2j)]

print(c[::-1])  #[(4+2j), 0j, 10.0, 'krishna', 1]

d=[1,2,3,40]
e=[5,6,7,8]
print(d+e)#[1,2,3,40,5,6,7,8]   # for concatination both operand must be of same datatype
print("kalraj"+"koteri")        #concatination supported by list and string both
# print(d-e)  this is an error

# print(d*e)  this is an error

# print(d/e)  this is an error 

print("1"+"kalraj")
# name='kalraj'
print(f'{1}{"name"}')
print('%s %s %s' %(1,'kalraj','koteri'))

#methods:

f=list()   #[]
print(f, type(f),id(f))

f.append(1)
print(f)
# f.append(1,2,3,4,5)   #TypeError: list.append() takes exactly one argument (5 given)
f.append([1,2,3,4,5])
print(f)

f.clear()    
print(f)     #[]   means empty list

f.extend([1,2,3,4,5])   # string and list both are iterable beacuse it support indexing 
print(f)
f.extend("krishna")
print(f)

print(f.index("k"))
f.extend("kkkkkkk")
print(f)      #[1, 2, 3, 4, 5, 'k', 'r', 'i', 's', 'h', 'n', 'a', 'k', 'k', 'k', 'k', 'k', 'k', 'k']

print(f.index('k'))

f.append(1000000000)
print("f",f)

z=f
print("z",z)

z.append(999999)
print("z",z)
print("f",f)

print("z",id(z))
print("f",id(f))

l=[1,2,3]
print("l",l,id(l))
m=l.copy()
print("m",m,id(m))
m.append(100000)
print("m",m)
print("l",l)

