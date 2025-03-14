a=[1,2,3,4,5,6]
print(a)
a.append(9)
a.append(6)
a.append("hi")#it just adds to the list irrespective of the data type and and it doesnt cares for the repetition
print(a)
# intendation can be done
print(a[0])
# insetion is also possible in lists
a.insert(0,11)# here 0 represents the location of a value
print(a)
#  value can be replaced by another value
a[0]=12
print(a)
# valued of a can be removed
a.pop(5)#5th element(index) is removed
print(a)
# what does a.pop() means
a.pop()
print(a)#the last element will be deleted
# a.extend is used to merge two lists
b=[2,90,80]
a.extend(b)
print(a)
