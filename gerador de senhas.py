import string
import random

letras_minusculas = string.ascii_lowercase
letras_maiusculas = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

caracteres = ""

senha = ""
numero_caracteres = 0
gui_principal = True

while gui_principal == True:
    print("Gerador de Senhas")
    print("Digite 3 para sair!")
    digitos = int(input("Quantos digitos você quer na sua senha? (minimo de 5 digitos) "))
    numero_caracteres = digitos
    if digitos >= 5:
        for _ in range(numero_caracteres):
            caracteres = random.choice(letras_maiusculas + letras_minusculas + numeros + simbolos)
            senha = senha + caracteres
        print(senha)
    elif digitos == 3:
        gui_principal = False
    else:
        print("Insira um numero acima de 5!")
        


    