# (REPETIÇÃO5) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, 
# de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. 
# O programa deverá apresentar os valores das duas temperaturas.

cont = 0
graus = 0
farenait = 0
while graus <= 100:

    farenait = (graus *1.8) + 32
    print(graus, "graus para farenait é", farenait)
    graus += 10