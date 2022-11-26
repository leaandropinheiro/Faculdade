'''Faça um programa que receba vários números, calcule e mostre:
- a soma dos números digitados;
- a quantidade de números digitados;
- a média dos números digitados; 
- o maior número digitado;
- o menor número digitado;
- a média dos números pares;
- a porcentagem dos números ímpares entre todos os números digitados.
Finalize a entrada de dados com a digitação do número 30000.
'''

par = impar = num = cont = soma = qnt = media = maior = menor = mediaPares = porcent = 0

print('Faça um programa que receba vários números, calcule e mostre:')
print('\n- a soma dos números digitados;')
print('- a quantidade de números digitados;')
print('- a média dos números digitados; ')
print('- o maior número digitado;')
print('- o menor número digitado;')
print('- a média dos números pares;')
print('- a porcentagem dos números ímpares entre todos os números digitados.\n')

while num < 30000:
    num = int(input('Insira um número: \n'))
    soma += num
    qnt += 1
    media = soma/qnt
    mediaPares = num/2


    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('\nA soma dos números digitados é: {}'.format(soma))
print('A quantidade de números digitados é: {}'.format(qnt))
print("A média dos números digitados é: {}".format(media))
print('\nO maior número digitado {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
print('\nA média dos números pares é: {}'.format(mediaPares))
print('\nAporcentagem dos números ímpares entre todos os números digitados é: {}'.format(porcent))