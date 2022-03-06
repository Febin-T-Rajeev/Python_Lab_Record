num = int(input('Enter in a value: '))
total = 0
for i in range(0, num):
    total += int(str(num) + i * str(num))
print(total)
