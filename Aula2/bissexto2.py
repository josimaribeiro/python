from calendar import isleap
from time import sleep


print("Usando método da classe isleap")

ano = int(input("Digite o ano: "))

print("Aguarde verificando...")
sleep(3)
if isleap(ano):
    print("É bissexto")
else:
    print("Não é bissexto")
