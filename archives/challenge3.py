# movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
import os
import csv
arquivo = os.path.join(r"C:\Users\JOAO", "list.csv")

with open(arquivo, "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])

