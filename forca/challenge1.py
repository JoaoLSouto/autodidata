import random

def hangman(word):
    erros = 0
    etapas = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\\     ",
             "|       / \\     ",
             "|               "
              ]
    
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while erros < len(etapas) - 1:
        print("\n")
        char = input("Adivinhe uma letra: ")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            erros += 1

        print(" ".join(board))
        print("\n".join(etapas[:erros + 1]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(etapas[:erros + 1]))
        print(f"Você perdeu! A palavra era '{word}'.")


words = ["paralelepipedo", "quadrado", "triangulo", "quente"]
random_word = random.choice(words)

hangman(random_word)
