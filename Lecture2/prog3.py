import time

n = 10000000
temp = []

start = time.time()
for i in range(0, n+1):
    if i % 2 == 0:
        temp.append(i**2)
    else:
        temp.append(i**3)

print(temp[:15])
print(time.time() - start)


start2 = time.time()
temp_new = [x**2 if x % 2 == 0 else x**3 for x in range(0, n+1)]
print(temp_new[:15])
print(time.time() - start2)
