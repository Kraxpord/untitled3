n = int(input('1Введіть число->'))
p = int(input('2Введіть число->'))
if p/2==0:
    p+=1
while p<n:
    print(f'{p}')
    p+=2
else:
    print('робота закінчена')
