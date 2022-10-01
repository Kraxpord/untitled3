p = int(input('1Введіть число->'))
g = int(input('2Введіть число->'))
temp = p
p = g
g = temp
while p>g:
    p-=1
    print(f'{p}')