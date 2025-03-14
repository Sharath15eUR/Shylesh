# write a program to get username and password from the user and check it with u=shylesh and p=123 if both  username and password matches with u=shylesh and p=123 print true else false.
u="shylesh"
p=123
username=input()
password=int(input())
def hello():
    if (username==u and p== password):
        return True
    else:
        return False
print(hello())
    
