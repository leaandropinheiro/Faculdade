'''(REPETIÇÃO7) Elaborar um programa que efetue a leitura sucessiva de valores numéricos
e apresente no final o total do somatório, a média e o total de valores lidos.
O programa deve fazer as leituras dos valores enquanto o usuário estiver fornecedor valores positivos.
Ou seja, o programa deve parar quando o usuário fornecer um valor negativo.'''

numero = int(input('Digite um novo número:'))
contador = 0
soma = 0
media = 0

while numero > 0:
        contador += 1
        soma += numero
        numero = int(input('Digite um novo número:'))

print(f'A soma dos numeros é igual a {soma}')
media = soma / contador
print(f'A média é igual a {media}')
    

    