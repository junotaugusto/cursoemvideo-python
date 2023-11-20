# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão sendo 1 - binário, 2 - octal e 3 - hexadecimal.

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Solicita ao usuário escolher a base de conversão
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite o número da opção desejada: "))

# Converte o número para a base escolhida
if opcao == 1:
    resultado = bin(numero)
elif opcao == 2:
    resultado = oct(numero)
elif opcao == 3:
    resultado = hex(numero)
else:
    print("Opção inválida. Escolha entre 1, 2 ou 3.")
    resultado = None

# Exibe o resultado
if resultado is not None:
    print(f"Resultado da conversão: {resultado}")
