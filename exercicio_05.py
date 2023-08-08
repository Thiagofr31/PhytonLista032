#Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
#números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
#multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
#do primeiro pelo segundo número.

num1 = int(input("Escolha um número: "))
num2 = int(input("Esolha outro número"))

soma = num1 + num2

sub = num1 - num2

sub2 = num2 - num1

mult = num1 * num2

div = num1 % num2

print(f"a soma dos dois números {soma}")
print(f"a subtração do primeiro pelo segundo número {sub}")
print(f" a subtração do segundo pelo primeiro número {sub2}")
print(f"a multiplicação entre os dois números {mult}")