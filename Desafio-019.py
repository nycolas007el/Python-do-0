'019'
'Um professor quer sortear um dos seus quatro alunos para apagar o quadro. '
'Faça um programa que ajude ele, lendo o nome dos quatro alunos e escrevendo na tela o '
'nome do escolhido.'
import random
n1 = str(input("Digite nome do aluno 1 : "))
n2 = str(input("Digite nome do aluno 2 : "))
n3 = str(input("Digite nome do aluno 3 : "))
n4 = str(input("Digite nome do aluno 4 : "))
alunos = [n1,n2,n3,n4]
print(f"Aluno escolhido foi {random.choice(alunos)}")