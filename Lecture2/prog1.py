

def mult_return(a, b, c):
    temp = [a, b, c]
    m = max(temp)
    mi = min(temp)
    aver = sum(temp) / len(temp)

    return (m, mi, aver)


Max, Min, Average = mult_return(4, 5, 2)
print(Max, Min, Average)


_, Min, _ = mult_return(-10, -20, -30)
print(Min)
