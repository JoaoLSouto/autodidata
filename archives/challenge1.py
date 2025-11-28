import os

caminho = os.path.join(r"C:\Users\JOAO", "st.txt")

with open(caminho, "r") as f:
    print(f.read())