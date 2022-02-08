f=open("hello.txt")
print(f.tell())
ho=f.readline()
print(ho)

f.seek(0)
print(ho)
print(f.tell())
f.close()