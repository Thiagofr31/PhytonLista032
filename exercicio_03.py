#Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
#programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros

kg = float(input("Qual seu peso em kg: "))
m = float(input("Qual a sua altura: "))

g = kg * 1000
cm = m * 100

print(f"Voce tem {g} gramas")
print(f"Você tem {cm} cm")