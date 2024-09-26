# Funcoes e Excecoes

def dividir():
    try:
        numerador = 20
        denominador = 2
        resultado = numerador / denominador
        print(resultado)

    except ZeroDivisionError:
        print("O valor não pode ser dividido por zero")

dividir()

