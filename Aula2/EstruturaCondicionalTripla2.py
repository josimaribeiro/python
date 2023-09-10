cor = input("Digite a cor do sinal : ")

match cor:
    case "vermelho":
        print("Pare")

    case "amarelo":
        print("Atenção")

    case "verde":
        print("Siga")

    case _:
        print("Você digitou uma cor errada")
