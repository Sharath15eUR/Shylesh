#its used to the group of data and the data can be list or tuple or a set
# the term before : is known as keys and the term after : is known as values
# , is most important after the values
# it is irrespective of the data types

a={"name" : "shylesh",
   50:34,
   "hello" : 4,
   "gender" : "male",
   "list":["see",9,8,4,4],
   "tuple":(1,2,3,3),
   "set":{1,0,8,9,8}}
print(a)
#inorder to print only the values
print(a.values())

#inorder to print only the keys
print(a.keys())
#replacing a value and removing a value can be done same command
a["name"]= "ram"#replacing a value
print(a)
a["color"]="red"#adding a new one
print(a)
#deleting a value and a key
a.pop("name")
print(a)
#a complete dictionary can be deleted.
#del a
#print(a)# error occurs here as the dictioary was deleted
#to clear a dictionary
a.clear()
print(a)


#stationary, printing values and keys ,
replacing, remove, add,delete , clear,
