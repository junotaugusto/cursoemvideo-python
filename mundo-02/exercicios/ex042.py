# Refaça o desafio 35.
# Mostre os lados do triangulo iguais : equilátero. Isósceles dois lados iguais. Escaleno todos diferentes. 

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print("Triângulo equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo Isóceles. Possui dois lados iguais.')
        
        # Identificar quais são os lados iguais
        if r1 == r2:
            print(f"Lados iguais: (1): {r1} e (2): {r2}")
        elif r1 == r3:
            print(f"Lados iguais: (1): {r1} e (3): {r3}")
        elif r2 == r3:
            print(f"Lados iguais: (2): {r2} e (3): {r3}")

    elif r1 != r2 != r3:
        print("Triângulo Escaleno")
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
