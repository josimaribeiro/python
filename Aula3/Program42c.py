# declare constants
TOTAL_DE_FUNCIONARIOS = 3


for x in range(TOTAL_DE_FUNCIONARIOS):
    mat = int(
        input("Digite a matricula do func " + str(x + 1) + "..................: ")
    )
    totalVendas = float(
        input("Digite o total das vendas do func " + str(x + 1) + " ..........: ")
    )
    comissaoFunc = totalVendas * 3 / 100
    print(
        "Comisssao func " + str(x + 1) + " .............................: ",
        comissaoFunc,
    )
    print("")
