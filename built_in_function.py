# dir() it will return all properties and method of the object without the value and also return buit_in properties which are default for all object 
class Person:
    name='johan'
    age=34
    country='india'
print(dir(Person))
print()
print()
print()
#delattr() this function will delete the attribute from the object
#syntax : delattr(object_name,attribute_name)
class Myclass:
    name="kalraj"
    age=28
    country='india'
    def pop(self):
        print('this is method')
obj=Myclass()
obj.country
delattr(Myclass,'country')
print(dir(Myclass))
#hasattr() it will show if attribute or method is present in object or not return true if present else false if not present
x=hasattr(Myclass,'country')

print(x)
print()
m=hasattr(Myclass,'pop')
print(m)
# print(obj.country)
# setattr() it will set the value of specified attribut to specific object
# Syntax : setattr(object,attribut,value)
setattr(Myclass,'country','india')
print(obj.country)
#getattr() it will return the specific attribute from the specified object
x=getattr(Myclass,'pop')
print(x)
p=divmod(5,2)
print(p)