#Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
#tela o valor do índice de massa corporal desta pessoa (IMC).
#Fórmula: IMC = peso / altura2
#- Obs: peso em quilos e altura em metros.

kg = float(input("Qual seu peso em kg: "))
m = float(input("Qual sua altura: "))

imc = kg % m**2

float(print("Seu índice de massa corporal desta pessoa (IMC) é: " , imc))




