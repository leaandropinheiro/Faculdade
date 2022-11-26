print ("digite o preco")
preco = float(input())

if preco <= 50:
    valau = preco * 50 / 100

else: 
    if preco > 50 and preco <= 100:
        valau = preco * 10 /100

    else:
        valau = preco * 15 /100


print ("o valor do aumento é", valau)


novopreco = preco + valau

print ("digite o novo preco")
novopreco = float(input())

if novopreco < 80:
    print("Barato")
else:
    if novopreco > 80 and novopreco <= 120:
        print ("normal")
    else:
        if novopreco > 120 and novopreco <= 200:
            print("Caro")
        else:
            if novopreco > 200:
                print("Muito Caro")
    

            