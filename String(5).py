#Important point about string 
# 1> String constructor is str()
# 2> String literal is string '', "", """""",''''''
# 3> String is a set of sequence of elements
# 4> String is immutable 
# 5> String support indexing
# 6> String support slicing 



# 1> String constructor is str()

a=str()
print(a)


b=""
print(b)

c=''         
print(c)
print(type(c),"c")


# 2> String literal is string '', "", """""",''''''

d=''
print("d",type(d),d)

e=""
print("e",type(e),e)

f=""""""
print("f",type(f),f)

g=''''''
print("g",type(g),g)

k="Rohan"
print(k)
print("k",type(k),k)

# 3> String is a set of sequence of character

l="KRISHNA"
print(l)

print(l[-4])
print(l[3])

# print(l[8])
print("Hello world")
print(l[2:6])
print(l[2:7])
print(l[2:7:1])
print(l[2:7:2])
print(l[0:7:1])
print(l[:7:1])
print(l[::1])
print(l[::1])
print(l[:])
# print(l[2343;3242334:1])

# negative indexing and slicing 

print(l[-6:-2:1])
print(l[-1:-8:-1])
print(l[::-1])
print(l[-1::-1])

print(l[1:-1:-1])

j="0123456789"
print(j[1:10:2])
print(j[1::2])

print(j[0::2])
print(j[::2])

m="krishna"
print(m.upper())
print(m)
print(m.capitalize())
print(m)
n="nNkRisHna714@gmail.com"
print(n.casefold())
