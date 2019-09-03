def func_name(a, b):
    print("Hey!")
    print(a+b)


# REQUIRED ARGS
#print(func_name(2, 1))


def func_another(a, b, c=1):
    return a+b+c


type(func_another)


def isPalindrome(text):
    return text == text[::-1]


print(isPalindrome('abba'))
