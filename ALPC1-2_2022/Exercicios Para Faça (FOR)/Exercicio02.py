import numpy as np 
contador = qntIdade = qntPess50y = mediaAltura = pPeso = 0

idade = []
altura = []
peso = []


'''
Faça um programa que receba a idade, a altura e o peso de 25 pessoas. 

Calcule e mostre:
- a quantidade de pessoas com idade superior a 50 anos
- a média das alturas das pessoas com idade entre 10 e 20 anos;
- a percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

'''

'''
for i in range(numPessoas):
    contador += 1
    print("\n{} ª pessoa".format(contador))
    idade = int(input("\nDigite sua da Idade: "))
    altura = float(input('Digite a sua altura: '))
    peso = float(input("Digite o seu peso: "))
    print('{}Obrigado!!!'.format())
'''

for i in range(0,2):
    print("\n{}ª pessoa".format(i+1))
    idade.append(int(input("\nDigite a Idade da {}ª pessoa: ".format(i+1))))
    altura.append(float(input('Digite a altura da {}ª pessoa: '.format(i+1))))
    peso.append(float(input("Digite o peso da {}ª pessoa: ".format(i+1))))
    if idade[i] > 50:
        contador += 1
    if peso[i] < 40:
        contador+=1


if contador ==1:
    print('\nExiste 1 pessoa acima de 50 anos.')
else:
    print('\nExistem {} pessoas acima de 50 anos'.format(contador))


print('A média das alturas é {:.2f} metros'.format(sum(altura)/len(altura)))

print('A percentagem de pessoas com peso inferior a 40 quilos é {} %'.format((pPeso)))