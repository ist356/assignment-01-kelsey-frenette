numbers = {'odd': [], 'even': []}
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    if num % 2 == 0:
        numbers['even'].append(num)
    else:
        numbers['odd'].append(num)

print(numbers)