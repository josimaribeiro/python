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

match codigoFuncao:
    case 100:
        print("Reajuste de..................: 2%")
        reaj = salarioBase * 2 / 100

    case 300:
        print("Reajuste de..................: 3%")
        reaj = salarioBase * 3 / 100

    case 400:
        print("Reajuste de..................: 5%")
        reaj = salarioBase * 5 / 100

    case 600:
        print("Reajuste de..................: 7%")
        reaj = salarioBase * 7 / 100

    case _:
        print("Digitou alguma cois errada")

print("Valor do reajuste............: %.2f " % reaj)
salarioLiquido = salarioBase + reaj
print("Valor do salariio liquido ...: %.2f " % salarioLiquido)
