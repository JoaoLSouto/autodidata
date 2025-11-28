import os

arquivo = os.path.join(r"C:\Users\JOAO", "answer.txt")
answer = input("quantos anos você tem?")

with open(arquivo, "w+") as f:
    f.write(answer) 
    f.seek(0)
    print(f.read())