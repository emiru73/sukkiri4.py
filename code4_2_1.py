count = 0
eat = True
print('カレーを召し上がれ')
while eat == True:
    count += 1
    print('{}皿のカレーを食べました'.format(count))
    eats = input('おかわりはいかがですか？(y/n) >>')
    if eats == 'y':
        continue
    else:
        break
print('ごちそうさまでした')