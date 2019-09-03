numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

print(numerator/denominator)

try:
    print(numerator/denominator)
except:
    print("Division by zero!")
