#append() method
list_a=[1,2,3,4,5,6]
new_value =60
print(type(new_value))
list_a.append(new_value)
print(list_a)
list_a=[1,2,3,4,5,6]
new_value =60,70  #its datatype by default become tuple if we assign more than one  value to variable
print(type(new_value))
list_a.append(new_value)
print(list_a)
#we can nested list which means we can put list inside list
list_b=[12,13,15,16]
list_c=[18,32,42]
list_b.append(list_c)
print(list_b)
print()
new_var=10
print('new_var datatype is :',type(new_var))
new_var=10,20,10
print('new_var datatype is :',type(new_var))
print()
#extend() method 
list_c=[10,40,50]
list_c.extend([10,20])
print(list_c)
print()
list_c.extend((20,30))
print(list_c)
print()
#insetion of ew value by indexing
list_insert=[10,20,40,50]
# list_insert[2:3]=[60,70]
print(list_insert)
list_insert[2:4]=[60,70]
print(list_insert)
#insert element by using method i.e insert() method
list_new=[10,'kalraj',50.0,07j]
print(list_new)
print()
list_new.insert(1,'koteri')
print(list_new)
#clean() method it will make empty list or literal
list_new.clear()
print(list_new)
#copy() method it will make another copy or duplicate of a lsit 
list_old=[10,20,30,40,50]
list_copy=list_old.copy()

print(list_old,id(list_old)) #[10, 20, 30, 40, 50] 2488308703936
print(list_copy, id(list_copy)) #[10, 20, 30, 40, 50] 2488308703808
#pop() method by using this method we can delete an element from the end it is bydefault and we can delete from specific index
list_old.pop()
print(list_old) #[10, 20, 30, 40]
#by usinf pop delete an element from specific position
print(list_old) #[10, 20, 30, 40]
list_old.pop(1)
print(list_old) #[10, 30, 40]
# del  it wil delete by index
print(list_copy) #[10, 20, 30, 40, 50]
del list_copy[1] 
print(list_copy) #[10, 30, 40, 50]
del list_copy[3]
print(list_copy) #[10, 30, 40]
print()
#remove() method it will delete the specific element from the list
print(list_copy)  #[10, 30, 40]
list_copy.remove(40)
print(list_copy)  #[10, 30]
# list_copy.remove(50)
# print(list_copy) #ValueError: list.remove(x): x not in list
#count() method it will return the number of time the element present in the list
list_count=[210,'kalraj',0j,'hello',210,0j,210,'hello']
print(list_count.count(210)) #3
print(list_count.count('hello')) #2 string 'hello' present in the list is 2 times
print(list_count) #[210, 'kalraj', 0j, 'hello', 210, 0j, 210, 'hello']
list_count.remove(210) # it will remove first occurrane of na element 
print(list_count) #['kalraj', 0j, 'hello', 210, 0j, 210, 'hello']

#index() it will return the index of first occurrence of the value in the list
print(list_count) #['kalraj', 0j, 'hello', 210, 0j, 210, 'hello']
x=list_count.index(210)
print(x) #3
#reverse() method it will reverse the order of element in list
print(list_count) #['kalraj', 0j, 'hello', 210, 0j, 210, 'hello']
list_count.reverse()
print(list_count) #['hello', 210, 0j, 210, 'hello', 0j, 'kalraj']
print()
#sort() method it will sort the list alphabetically
list_sort=['kalraj','hello','raj','balraj']
list_sort.sort()
print(list_sort) #['balraj', 'hello', 'kalraj', 'raj']
list_sort.sort(reverse=True)  #['raj', 'kalraj', 'hello', 'balraj'] by default reverse= False which means it will order the element in assending order and if we will write reverse=True it will sort element in descending order

print(list_sort)
print()
# looping list
# list_loop=[30,300,10,'raj'] # sort method supprt only same type of datatype
# list_loop.sort()             
# print(list_loop) #TypeError: '<' not supported between instances of 'str' and 'int'
list_loop=[10,30,20,'kalraj']
for x in list_loop:
    print(x)
for x in range(len(list_loop)):
    print(list_loop[x])
#during pushing file into git occur this error ! [rejected]        master -> master (fetch first)
# error: failed to push some refs to 'https://github.com/kalraj/python_wd_classes.git' then fetch the origin master in a another branch and make rebase then push it  abd delete the branch 
# git fetch origin master:temp
#git rebase temp
#git push origin HEAD:master
#git branch -D temp