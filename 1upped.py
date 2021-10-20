x = 1
n = 2
m = 3
s = 4
l = 0
p = 0
print('Как вас зовут?')
a = (input())

print('Приветствую вас,', a)

print('Введите свой возраст:')
b = (input())

print('Ваш любимый цвет? (1 – красный, 2 – зеленый, 3 – синий)')
c = int(input())

print('Ваша любимая музыка? (1 – классика, 2 – поп-музыка, 3 – рок)')
d = int(input())

print('Ваше любимое время года? (1 – осень, 2 – зима, 3 – весна, 4 – лето)')
e = int(input())

print('Вы любите видеоигры? (1 - да, 2 - нет, 3 - не знаю) ')
j = int(input())

if j == n or j == m:
    p = l - 5
else:
    l = 1

if (c == x or c == m) and d == m and j == x:
    l = 2 + p
elif c == n and (d == x or d == n) and j == x:
    l = 2 + p
elif c == n and d == m and (j == n or j == m):
    l = 2 + p
elif (c == x or c == m) and (d == x or d == n):
    l = 0 + p
elif (c == x or c == m) and (d == x or d == n) and j == x:
    l = 1 + p
elif (c == x or c == m) and d == m:
    l = 1 + p
elif c == n and (d == x or d == n):
    l = 1 + p
else:
    l = 2 + p

if l == 3:
    print('we will be friends')
elif l == 2:
    print('we will be friends')
else:
    print('we dont will be friends')
