# loop1= for i in range(100)
# print(type(loop1))
# h="yogendra"
# ier=iter(h)
# print(ier.__next__())
# for i in h:
#     print(i,end="")

def gen(n):
    for i in range(1,n):
        yield i

h=gen(5)
for i in h:
    print(i)