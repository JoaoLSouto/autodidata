#6 Adicione uma docstring a todas as funções que escreveu nos desafios 1-5.

#1 
def quadrado(x):
    """ Divide o valor X por 2  retorna o resultado """
    return x ** 2
print(quadrado(2))

#2.

def exibir_strg (string):
    """ Exibe a string recebida como parâmetro """
    print(string)
exibir_strg(1)
    
#3 

def parametros(x, z, y, a=0, b=0):
    """Recebe 3 parametros obrigatórios 2 dois opcionais e exibe"""

    print("Os obrigatórios são:", x, y, z, "e os opcionais são:", a, b)

parametros(1, 2, 3, 4, 5)
parametros(1, 2, 3)



#4 

def primeiro_inteiro (x):
    """Divide o valor x por 2 e retorna o resultado """
    return x/2 
print(primeiro_inteiro(2))

def segundo_inteiro (x):
    """Multiplica o valor x por 4 e retorna o resultado """
    return x*4

y = primeiro_inteiro(4)
z = segundo_inteiro (y) 
"""Z é igual o valor do Y que será multiplicado por 4"""
print(y)
print(z)

#5 .
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)

