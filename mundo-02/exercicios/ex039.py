# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade:
# Se ele vai se alistar ao serviço militar. Se é a hora de se alistar. Se ja passou do tempo do alistamento. Seu programa também deve mostrar o tempo que falta ou o tempo que já passou para o alistamento.

while True:
    try:
        ano_Nascimento = int(input("Qual o ano do seu nascimento? Digite: "))
        if ano_Nascimento <= 2023:
            print(f"Você nasceu em {ano_Nascimento}. ")
            ano_Alistamento = 2023 - ano_Nascimento
            if ano_Alistamento > 18:
                print(f"Você não se alistou ainda? Já está com {ano_Alistamento} anos! Passaram {ano_Alistamento - 18} anos desde a data limite do seu alistamento.")
            elif ano_Alistamento < 18:
                print(f"Ainda não está na hora de se alistar. Faltam {18 - ano_Alistamento} anos para o seu alistamento.")
            elif ano_Alistamento == 18:
                print(f"Acabou de completar 18 anos? Você precisa se alistar neste ano de 2023! Não perca tempo.")
            break
        else:
            print("Ano de nascimento inválido. Tente novamente: ")
    except ValueError:
        print("Por favor, digite um ano válido: ")