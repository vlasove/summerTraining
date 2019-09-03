import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6]
y = [i**2 for i in x]


plt.scatter(x,y, color = 'b', label = "Quadratic")

plt.plot(y,x, color ='r', label = "Exponent")
plt.axis([0,100, -10,40])
plt.legend()
plt.title('My Title!')
plt.xlabel('This is X')
plt.ylabel('This is Y')
plt.grid(True)

plt.show()