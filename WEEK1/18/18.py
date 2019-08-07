n = int(input())
h = n // 3600
m = n // 60 - h * 60
s = n - h * 3600 - m * 60
print(h % 24, ':', sep='', end='')
print(str(m // 10) + str(m % 10), ':', str(s // 10) + str(s % 10), sep='')
