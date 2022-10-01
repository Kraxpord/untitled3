n = int(input("Введіть число1->"))
p = int(input("Введіть число2->"))
if n>p:
    g = n
    n = p
    p = g
elif n%2==0:
    n +=1
while n < p:
    print(f"{n}")
    n+=1
else:
    print('робота цикла завершина')
    print('робота програми завершина')
