#idade = int(input("Insira sua idade: "))

#if idade >= 18:
    #print("Você já é maior de idade")
#elif idade >= 16 < 18:
    #print("Você pode votar, mas é menor de idade")
#else:
    #print("Você ainda não pode votar")


#while idade < 18:
    #idade = idade + 1
    #print(f"Um ano se passou!, sua idade é {idade}")
#print("Agora você tem 18 anos!")



#lista_nomes = [
    #"Ana",
    #"João",
    #"Maria",
    #"Pedro"
##]

#for nomes in lista_nomes:
    #print(f"Olá, {nomes}, você está convidado!")


#numeros = [
    #1,
    #2,
    #3,
    #4,
    #5,
    #6,
    #7,
    #8,
    #9,
    #10
#]
#print(numeros)
##for numero in numeros:
    ##if numero % 2 == 0:
        ##print(f"{numero} É um número par")
    ##else:
        ##print(f"{numero} Não é par")
    
#def checar_par_impar(numeros):
    #for numero in numeros:
        #if numero % 2 == 0:
            #return("Número Par")
        #else:
            #return("Número Impar")
    
#resultado_par_impar = checar_par_impar(numeros)
#print(resultado_par_impar)




lista_numeros = []

numeros = input("Insira uma lista de números com espaços: ")
partes = numeros.split()
for p in partes:
    lista_numeros.append(int(p))

#print(lista_numeros)

#for numero in lista_numeros:
    #lista_resultados = []
    #if numero % 2 == 0:
        #lista_resultados.append("Número Par")
    #else:
        #lista_resultados.append("Número Impar")

print(lista_numeros)
def checar_par_impar(lista_numeros):
    lista_resultados = []
    for numerozao in lista_numeros:
        if numerozao % 2 == 0:
            lista_resultados.append("Número Par")
        else:
            lista_resultados.append("Número Impar")
    return lista_resultados

resultados = checar_par_impar(lista_numeros)
print(resultados)





