la=[i for i in range(67)]
print(la)
print(type(la))
o=type(la)
print(o)







ho={i:f"item-{i}" for i in range(100) if i%2==0}
print(ho)
print(type(ho))

yo={i for i in ["hari","yogendra","rejina","labahang","yogendra"]}
print(yo)
print(type(yo))

hero=(i for i in ["hari","yogendra","rejina","labahang","yogendra"])
print(hero.__next__())
print(hero)
print(type(hero))