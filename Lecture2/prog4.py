def myFunc(a, b):
    return a+b


def anotherFunc(a, b):
    return a**2 - b**3



anonFunc = lambda a,b: a+b
print(anonFunc(2,3))

print(type(myFunc))
print(type(anonFunc))





for i in range(0,1000):
    print((lambda x : x**3 + 2)(i))
