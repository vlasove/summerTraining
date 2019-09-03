class MyClass:
    def __init__(self, a,b,c):
        self.A = a
        self.B = b 
        self.C = c

    def __my_func(self):   #method
        print("Hey!")
        print(self.A, self.B,self.C)



m1 = MyClass(1,2,10)
m2 = MyClass

print(type(m1))
print(type(m2))

m1.A = 10
m1.B = 200

print(m1.A, m1.B)
m1.__my_func()
