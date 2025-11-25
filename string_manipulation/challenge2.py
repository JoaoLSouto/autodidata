#2. Escreva um programa que colete duas strings com um usuário, insira-as na string 
# "yesterday I wrote a [...]. I sent it to [...]!" e exiba uma nova string

input1 = input("O que você escreveu?: ")
input2 = input("para quem você mandou?: ")

fullphrase = "Yesterday I wrote a "+input1+". I sent it to "+input2+"!"
print(fullphrase)