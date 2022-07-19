def isEven(value):
    res = (value >> 1) << 1
    if res == value:
        return 1
    return 0

value = input()
print(isEven(int(value)))
