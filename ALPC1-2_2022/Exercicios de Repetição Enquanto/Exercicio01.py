'''
Faça um algoritmo que calcule a multiplicação de dois números inteiros sem utilizar o operador “*”. 
Em vez disso, utilize apenas o operador de adição “+”. Para implementar esse algoritmo, 
devemos lembrar que qualquer multiplicação pode ser expressa por meio de somas. Por exemplo, 
o resultado da expressão 6 * 3 é o mesmo que 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. 
Ou seja, soma-se um elemento com ele próprio o número de vezes do segundo elemento.
'''


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
total = 0
for x in range(1, num2 + 1):
    total += num1

print('a multiplicação dos dois números inteiros é: {}'.format(total))