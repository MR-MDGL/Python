def remove(numbers, target):
    while target in numbers:
        numbers.remove(target)
    return numbers

input = [1, 2, 5, 3, 5, 4, 5, 6]
target = 5
result = remove(input, target)
print(result)
