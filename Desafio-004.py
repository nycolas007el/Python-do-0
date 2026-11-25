'004'
'Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as '
'informações possíveis sobre ele (se é numérico, se é texto, se só tem espaços, se está em '
'maiúsculas, etc.), usando os métodos de teste que acabamos de ver e a sua linda f-string!'
algo = input("Digite qualquer coisa ")

print("O tipo primitivo desse valor é : ", type(algo))
print("Só tem espaços?", algo.isspace())
print("É número?",algo.isnumeric())
print("É alfabetico (Só letras)?", algo.isalpha())
print("É alfanumerico (Números e letras)?", algo.isalnum())
print("Está maiúsculas?",algo.isupper())
print("Está minúsculas?",algo.islower())
print("Está capitalizada (com a primeira maiuscula)?",algo.istitle())