"""
While em Python   - Aula 7
utilizado para executar uma
condicao enquanto ela for verdadeira

Requisitos: entender condicoes e operadores

"""
contador = 1
acumulador = 1

while contador <= 10: # execucao infinita
    print(contador,acumulador)
    if contador > 5:
        break

    acumulador = contador + acumulador
    contador += 1
else:
    print('Cheguei no else')
