# import time
# from functools import lru_cache

# @lru_cache(maxsize=3)
# def ro(n):
#     time.sleep(n)
#     return n

# print("my name is yogedra khapangi")
# ro(3)
# print("my name is magar")
# ro(3)
# print("iam coder man")
# ro(3)
# print("iam sofrware engineer")

a=(input("Enter first number."))
b=(input("Enter the second number."))

    
try:
    print(int(a)+int(b))

except Exception as e:
    print(e)


print("this is importent function. ")