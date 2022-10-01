p = int(input('1Введіть число->'))
g = int(input('2Введіть число->'))
if p%2==1:
    p+=1
while p<g:
    print(f'{p}')
    p+=2
else:
    print('робота закінчена')