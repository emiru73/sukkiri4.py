numbers = [1,1]
data = sum(numbers)
while True:
    # Pythonでは-1は最後の数字、-2はその前の数字
    next =numbers[-1] + numbers[-2]

    if next <= 1000:
        numbers.append(next)
    else:
        break
print(numbers)