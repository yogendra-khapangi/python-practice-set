class Em:
    name="yogendra"
    @classmethod
    def change(cls,name):
        cls.name=name

yo=Em()
yo.name='khapangi'
print(yo.name)
print(Em.name)
yo.change("magar")
print(Em.name)