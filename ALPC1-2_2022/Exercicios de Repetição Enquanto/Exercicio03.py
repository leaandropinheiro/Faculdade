'''
Faça um algoritmo que calcule a soma de todos os números ímpares 
dentro de uma faixa de valores determinada pelo usuário. 
Um número é ímpar quando sua divisão por 2 não é exata, ou seja, 
o resto resultante da divisão inteira pelo número 2 tem valor 1. 
Utilize a palavra resto como operador que calcula o resto da divisão 
de um numero por outro.
'''

soma = 0
n = int(input('Digite um número: '))


while n < 0:
    