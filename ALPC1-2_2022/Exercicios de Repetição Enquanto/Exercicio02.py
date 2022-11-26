'''
Faça um algoritmo que leia um número inteiro e calcule o seu fatorial. 
Se o número for negativo, informe que o valor é inválido. 
Sabemos que o fatorial de um número n, representado por n!, é dado por:
n * (n-1) * (n-2) * ... * 1, para n > 0 e n! = 1 para n = 0
'''


n = 0
f = 1



n = int(input('Digite um número: '))
while n > 0:
    print('{}'.format(n), end=' ')
    print(' x ' if n > 1 else '=', end=' ')
    f *= n
    n -= 1
print('{}' .format(f))
if n < 0:
        print('você digitou o numero errado!')
