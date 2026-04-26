import random
dificuldade = input("fácil, médio ou difícil? ")

if dificuldade == "facil":
    numero_secreto = random.randint(1, 10)

elif dificuldade == "medio":
    numero_secreto = random.randint(1, 30)

elif dificuldade == "dificil":
    numero_secreto = random.randint(1, 50)

else:
    print("dificuldade inválida")

while True:
    chute = int(input("digite um numero: ") )
    if chute == numero_secreto:
        print ("voce acertou!")
        break
    elif chute > numero_secreto:
        print ("é menor")
    else: 
        print ("é maior")
