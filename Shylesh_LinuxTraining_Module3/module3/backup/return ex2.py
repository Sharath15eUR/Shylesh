# to write a program to implement (a+b)*c in which a+b should be done by a seperate function1 and the result of function1 is multiplied with c and printed
a=int(input())
b=int(input())
c=int(input())
def hello(num1,num2):
    return num1+num2
add=hello(a,b)
print(add*c)

