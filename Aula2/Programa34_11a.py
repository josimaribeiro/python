print("Cod. Func\tReajuste")
print("___________________________________________")
print("100\t\tReajuste de 2%")
print("300\t\tReajuste de 3%")
print("400\t\tReajuste de 5%")
print("600\t\tReajuste de 7%")
print("___________________________________________")
salarioBase = float(input("Salario  Base................: "))
codigoFuncao = int(input("Codigo da funcao.............: "))
salarioLiquido = 0.0
reaj = 0.0
if codigoFuncao == 100:
    reaj = salarioBase * 2 / 100
elif codigoFuncao == 300:
    reaj = salarioBase * 3 / 100
elif codigoFuncao == 400:
    reaj = salarioBase * 5 / 100
elif codigoFuncao == 600:
    reaj = salarioBase * 7 / 100
else:
    print("Digitou alguma coisa errada")

print("Valor do reajuste............: %.2f " % reaj)
salarioLiquido = salarioBase + reaj
print("Valor do salariio liquido ...: %.2f " % salarioLiquido)
