'Crie um programa que leia um número Real qualquer pelo teclado (ex: 6.127) e mostre na '
'tela a sua porção inteira.'
import math 
n1 = float(input("Digite um número real : "))
print(f"Seu número real é {n1} e seus resultado aproximado é de {math.trunc(n1)}")