list1=["hello","yogendra","khapangi","magar","my friend name is labhahang.",[1,5,6,4,8,9,2,3,4],87]

def fun1(*list1):
    """This is the function for to itrate changing list."""
    for item in list1:
        print(item)


fun1(*list1)
print(fun1.__doc__)