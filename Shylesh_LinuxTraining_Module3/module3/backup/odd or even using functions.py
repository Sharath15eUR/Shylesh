# to write a program to find the number is odd or even while calling the function( the input should gotten by calling part)
def find(msg):#defining part
    if (msg%2 ==0):
        print("even")
    if(msg%2 ==1):
        print("odd")
find(int(input()))#calling part
             
# if the function name is same on calling part and the defining part then the contents inside the () will get equal
#int(input())= msg
