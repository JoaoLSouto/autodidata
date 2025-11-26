numbers = [1, 3, 5, 7, 9, 11]

while True:
    print("Digite 'q' para sair")
    answer = input("chute um numero!: ")
    if answer == "q":
        print("Você saiu")
        break
    convert = int(answer)
    if convert in numbers :
            print("Parabéns! você acertou.")
    else:
        print("Errou! tente novamente.")