'018'
'Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente '
'desse ângulo.'
import math
angulo = float(input("Digite um ângulo : "))
n1 = math.radians(angulo)
print(f"Seu angulo {angulo} tem o correspondentemente SENO COSSENO TANGENTE {math.sin(n1):.2f} {math.cos(n1):.2f} {math.tan(n1):.2f}")