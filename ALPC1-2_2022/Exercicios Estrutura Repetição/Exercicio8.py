'''(REPETIÇÃO8) Elaborar um programa que
efetue a leitura de valores positivos inteiros
até que um valor negativo seja informado.
Ao final deve ser apresentados o maior e o
menor número informado pelo usuário.'''


num = int(input('Digite um valor: '))
contador = 0
maior = 0
menor = 0
quant = 0

while num > 0:
    contador += 1
    num = int(input('Digite um valor: '))
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('\nO maior numero foi {} e o menor numero foi {}'.format(maior, menor))


