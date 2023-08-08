#Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
#ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
#exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
#do mê

nome = (input("Fale o nome de um vendedor: "))
salario = int(input("Fale o salário fixo: "))
vendas = int(input("E o total de vendas efetuadas no mês: "))


comissao = vendas + (vendas*0.15)
sf = comissao + salario

print(f"Nome: {nome}\nSalário bruto: R${salario:.2f}\nComissão: R${comissao:.2f}\nSalário Completo (fixo + comissão sobre vendas): R${sf:.2f}")