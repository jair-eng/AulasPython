"""
Operadores relacionais

== Igualdade    > Maior que                  >= Maior ou igual que
< Menor que     <= Menor ou igual que     != Diferente

"""
idade_menor = 20
idade_maior = 30

nome = input("Qual e o seu nome? ")
idade = input("Qual e a sua idade? ")
idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
     print(f'{nome}  pode pegar Emprestimo')

else:
     print(f'{nome} não pode pegar emprestimo')