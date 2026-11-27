'015'
'Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a'
'quantidade de dias pelos quais ele foi alugado.'
'Calcule o preço a pagar, sabendo que:'
'O carro custa R$ 60,00 por dia.'
'O carro custa R$ 0,15 por Km rodado.'

n1 = float(input("Digite a quatidade de Km percorridos : "))
n2 = float(input("Digite a quantidade de dias que o carro foi alugado : "))
print(f"O preço que deve ser pago é de R${(n1*0.15)+(n2*60):.2f}")