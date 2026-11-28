'022'
'Crie um programa que leia o nome completo de uma pessoa e mostre:'

'O nome com todas as letras maiúsculas.'
'O nome com todas as letras minúsculas.'
'Quantas letras ao todo (sem considerar os espaços!).'
'Quantas letras tem o primeiro nome.'

n1 = str(input("Digite o seu nome completo :"))
print(f"{n1.upper()}")
print(f"{n1.lower()}")
print(f"{len(n1) - n1.count(' ')}")
dividido = n1.split()
print(f"{dividido[0], len(dividido[0])}")