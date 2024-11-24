def remove(numbers, target):
    while target in numbers:
        numbers.remove(target)
    return numbers

input_list = [1, 2, 5, 3, 5, 4, 5, 6]
target_number = 5
result = remove(input_list, target_number)
print(result)
