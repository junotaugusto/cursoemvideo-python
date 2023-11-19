"""
Condições aninhadas.
Condições aninhadas em Python significa colocar uma estrutura condicional dentro de outra. 
Você usa isso quando precisa verificar várias condições de maneira sequencial. Seguem exemplos desta aula prática abaixo.

Estrutura Condicional Composta:

Uma estrutura condicional composta, em programação, refere-se a um bloco de código que é executado com base em uma condição específica. 
Em Python, a estrutura condicional composta geralmente é implementada usando a instrução if, seguida por um bloco de código indentado, e opcionalmente pelas instruções else e elif (abreviação de "else if").

"""
nome = str(input("Digite seu nome: ")).capitalize() #letra maiuscula para o caso do usuário escrever sem letra maiúscula.
if nome == "Junot":
    print("Que nome bonito!")
elif nome == "Maria" or nome == "José" or nome == "Paulo":
    print(f'{nome}, seu nome é muito popular no Brasil.')
elif nome in 'Angela Junot Lucas Renata André':
    print(f'Eu conheço você, {nome}!')
else:
    print(f"{nome}, seu nome é normal.")
print(f'Tenha um bom dia, {nome}!')

