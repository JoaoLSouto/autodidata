# 1. Escreva uma função que receba um número como entrada e retorne esse número ao quadrado

def quadrado(x):
    return x ** 2
print(quadrado(2))

#2. Crie uma função que receba uma string como parâmetro e a exiba.

def exibir_strg (string):
    print(string)
exibir_strg(1)
    
#3 Escreva uma função que receba três parâmetros obrigatórios e dois parâmetros opcionais

def parametros(x, z, y, a=0, b=0):
    print("Os obrigatórios são:", x, y, z, "e os opcionais são:", a, b)

parametros(1, 2, 3, 4, 5)
parametros(1, 2, 3)



#4 Escreva um programa com duas funções. A primeira função deve receber um inteiro como parâmetro e 
# retornar o resultado do inteiro dividido por 2. A segunda função deve receber um inteiro como parâmetro e 
# retornar o resultado do inteiro multiplicado por 4. Chame a primeira função, salve o resultado como uma
# variavel e passe-a como parâmetro para a segunda função

def primeiro_inteiro (x):
    return x/2 
print(primeiro_inteiro(2))

def segundo_inteiro (x):
    return x*4

y = primeiro_inteiro(4)
z = segundo_inteiro (y)

print(y)
print(z)

#5 Escreva uma função que converta uma string em um float e retorne o resultado. 
# Use a manipulação de exceções que pode occorer.
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)

