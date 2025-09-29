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




#lista_numeros = []

#numeros = input("Insira uma lista de números com espaços: ")
#partes = numeros.split()
#for p in partes:
    #lista_numeros.append(int(p))

#print(lista_numeros)

#for numero in lista_numeros:
    #lista_resultados = []
    #if numero % 2 == 0:
        #lista_resultados.append("Número Par")
    #else:
        #lista_resultados.append("Número Impar")

#print(lista_numeros)
#def checar_par_impar(lista_numeros):
    #lista_resultados = []
    #for numerozao in lista_numeros:
        #if numerozao % 2 == 0:
            #lista_resultados.append("Número Par")
        #else:
            #lista_resultados.append("Número Impar")
    #return lista_resultados

#resultados = checar_par_impar(lista_numeros)
#print(resultados)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# A PARTIR DE AQUI É TUDO POO, PROGRAMAÇÃO ORIENTADA A OBJETOS.


# Com a POO, você aprende a organizar seu código em Classes e Objetos.
# Pense em uma Classe como um molde (por exemplo, o molde de um Carro).
# Pense em um Objeto como uma instância desse molde (seu Carro Vermelho ou o Carro Azul do vizinho).



# Pense assim:
# Um Objeto é uma pessoa concreta (como "João" ou "Maria").
# Em POO, a palavra técnica para criar um Objeto a partir de uma Classe é instanciar.
# A utilidade da POO é dar dados específicos (atributos) a cada objeto.

#class Pessoa: # A Classe Pessoa é a ideia de uma pessoa.
    #pass



#joao = Pessoa()
#joao.idade = 30 # agora joão tem 30 anos
#joao.profissão = "Engenheiro" # agora joão é engenheiro

#maria = Pessoa()
#maria.idade = 25
#maria.profissão = "Cientista de Dados"

#print(joao.profissão)
#print(maria.idade)

#Em projetos reais, isso não é prático. O certo é que a pessoa já "nasça" com seus atributos.
#Para isso, usamos um método especial chamado __init__ (lê-se "dúnder init"). Ele é o construtor da classe: 
#tudo o que está dentro dele é executado automaticamente no momento em que você cria o objeto.
#Sintaxe do Construtor
#Ele recebe o objeto que está sendo criado (self) e os dados que você quer passar (nome, idade, etc.):

class Pessoa:
    def __init__(self, nome, idade, profissão): # SEMPRE USAR O SELF, O SELF É INDESCARTÁVEL.
    # 'nome' é o objeto em construção (o futuro 'joao')
        self.nome = nome
        self.idade = idade
        self.profissão = profissão

    def apresentar(self):
        print(f"Olá, sou {self.nome}, tenho {self.idade} anos, e trabalho com {self.profissão}")

joao = Pessoa("João", 30, "Engenheiro")
maria = Pessoa("Maria", 25, "Cientista de Dados")

maria.apresentar()
print(maria.profissão)

# HERANÇA EM POO


class Pessoinha(Pessoa):
    pass
# Usando isso, a classe Pessoinha vai herdar TUDO da classe mãe, que é a Pessoa, fazendo assim, 
# com que tudo que esteja dentro da Pessoa, funcione aqui na Pessoinha.
# A herança só é útil quando a classe filha precisa fazer algo a mais ou de forma diferente da classe mãe.








