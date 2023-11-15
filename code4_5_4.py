day = 0
error = 0
for data in temp_new:
    if isinstance(data,float):
        error += 1
        day = day + data
        print(f'{day / (len(temp_new) -error):.2f}')