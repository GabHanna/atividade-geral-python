# Lacos

numero = int(input("Digite um número inteiro: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")