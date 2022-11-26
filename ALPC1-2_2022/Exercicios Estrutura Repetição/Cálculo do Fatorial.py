n = int(input('Digite uim numero para calcular seu Fatorial: '))

f = 1
print('Cálculo do Fatorial {}! = ' .format(n), end='')  

while n > 0:
    print('{}'.format(n), end=' ')
    print(' x ' if n > 1 else '=', end=' ')
    f *= n
    n -= 1
print('{}' .format(f))