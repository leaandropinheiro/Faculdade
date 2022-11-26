print("Digite o valor de N")
n = int(input())

contador = 0
while contador < n:
  print("Digite o fatorial desejado")
  fat = int(input())
  print(f"{fat}!", end=" ")
  result = 1
  while fat > 0:
    #print ("\t", fat)
    result *= fat
    fat -= 1
  print(f" = {result}")

  contador += 1
