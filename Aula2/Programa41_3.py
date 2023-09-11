def case_1_to_4():
    return "Insuficiente"


def case_5_to_6():
    return "Regular"


def case_7_to_8():
    return "Bom"


def case_9_to_10():
    return "Excelente"


def default_case():
    return "Valor inválido"


def switch_case_interval(value):
    cases = {
        (0, 4.9): case_1_to_4,
        (5.0, 6.9): case_5_to_6,
        (7.0, 8.9): case_7_to_8,
        (9.0, 10.0): case_9_to_10,
    }
    for (start, end), case_function in cases.items():
        if start <= value <= end:
            return case_function()
    return default_case()


# Example usage:


matricula = int(input("Codigo a matricula.........: "))
nota1 = float(input("Primeira nota....: "))
nota2 = float(input("Segunda nota.....: "))
media = (nota1 + nota2) / 2

print("Media : ", media)


result = switch_case_interval(media)
print(result)
