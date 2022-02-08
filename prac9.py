def summing(n1,n2):
    return n1+n2

def ss(string):
    return f"hello {string} are you fine?"
    
print("External module is ",__name__)
if __name__=='__main__':
    to=summing(3,4)
    print(to)
    print(ss("yogendra"))