
# 4 - Escreva um programa que permita que o usuário pergunte sua altura, cor favorita ou autor favorito e retorne 
# o resultado a partir do dicionário criado no desafio anterior

infos = {
    "altura": "1.73",
    "cor favorita": "Gray",
    "autor favorito": "Bauman",
}

while True:
    resposta = input("Tente adivinhar minha altura, cor favorita ou autor favorito: ").strip()

    correct = False

    if resposta in infos.values():
        
        for key, valuer in infos.items():
            if valuer == resposta:
                print(f"Acertou! Minha/Meu {key} é: {valuer}")
                correct = True
                break
        if correct:
            break
    else:
        print("Errou! Tenta de novo...")