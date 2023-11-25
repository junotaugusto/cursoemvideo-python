# A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos - Mirim. Até 14 anos - Infantil. Até 19 anos - Junior. Até 20 anos - Sênior. Acima: Master.

while True:
    try:
        anos = int(input("Digite o ano completo do seu nascimento: "))
        if anos > 2023:
            print("Erro! Digite um ano igual ou menor do que 2023.")
        else:
            if anos < 1900:
                print(f"Acho que você digitou sua idade errado. Você tem {2023 - anos} anos de idade? Digite corretamente da próxima vez.")
                print("Encerrando programa.")
                break
            else:
                idade = 2023 - anos
                if idade <= 9:
                    print(f'Você está na categoria MIRIM. Tem {idade} anos.')
                elif 9 <= idade <= 14:
                    print(f'Você está na categoria INFANTIL. Tem {idade} anos.')
                elif 14 <= idade <= 19:
                    print(f'Você está na categoria JUNIOR. Tem {idade} anos.')
                elif 19 <= idade <= 20:
                    print(f'Você está na categoria SÊNIOR. Tem {idade} anos.') 
                elif idade > 20:
                    print(f'Você está na categoria MASTER. Tem {idade} anos.')   
                break
    except:
        print("Idade inválida! Digite somente números.")