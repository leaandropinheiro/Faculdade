# REPETIÇÃO2) Elabore um programa que apresente no final o 
# somatório dos valores pares existentes na faixa de 1 até 500.


cont = 0
tot = 0

while cont <= 500:
    if cont % 2 == 0:
        end=" "    
        tot = tot + cont
    cont += 1
    print(tot, end=" ")