def multiplication(number):
    return number * 2


numbers = [1, 2, 3, 4, 5]

print(list(map(multiplication, numbers)))
print(list(map(lambda x: x * 2, numbers)))
