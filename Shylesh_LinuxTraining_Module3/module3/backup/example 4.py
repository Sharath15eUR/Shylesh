a=int(input())
b=int(input())
count=0
#if we want to count the values in i then the syntax is
#count=0//initialise
#count=count+1//increment
#print(count)//print

count1=0
for i in range(a,b):
    if(i%2==0):#even
        count=count+1
print(count)
for i in range(a,b):
    if(i%2==1):#odd
        count1=count1+1
print(count1)
