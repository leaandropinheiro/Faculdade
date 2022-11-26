# (REPETIÇÃO6) Elaborar um programa que efetue a leitura de 10 valores numéricos e 
# apresente no final o total do somatório e a média do total.


contador = 0
tnumeros = 0
resultado = 0

while contador < 10:
    num = int(input('Digite um valor:'))
    tnumeros += num
    contador += 1

resultado = tnumeros / contador

print(f"O somatório é: {tnumeros}")
print (f"A média total é {resultado}")