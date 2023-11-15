numbers = [1,1]
data = sum(numbers)
count = 2
while data <= 1000:
    numbers.append(data)
    data = data + numbers[count-1]
    count += 1

ratios = list()
for count in range(len(numbers)):
    if count == len(numbers) -1:
        break
    ratios.append(numbers[count+1] / numbers[count])
    print(ratios)



