#  Crie uma função que receba dois números e retorne o maior deles.
def maiorNumero(num1:int,num2:int)->int:
    if num1 > num2:
        return num1
    else:
        return num2

print(maiorNumero(50,8))  


# Calcule a média aritmética dos valores contidos em uma lista.
numberList = [1,10,5,8,20,30,6,2]

def calculaMedia(list):
    soma = 0
    for valor in list:
        soma += valor
    return soma / len(list)


print(calculaMedia(numberList))


# Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. 
listName=["José", "Lucas", "Nádia", "Fernanda","Parangaricuritimirruaro", "Cairo", "Joana"]

def maiorNomeDaLista(list):
    tamanho_nome = 0
    maior_nome = ''

    for nome in list:
        if len(nome) > tamanho_nome:
            tamanho_nome = len(nome)
            maior_nome = nome

    return maior_nome            

print(maiorNomeDaLista(listName))


#  Dada uma lista, descubra o menor elemento.
new_list_number = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]

def menorValor(list):
    list.sort()
    return list[0]
    

print(menorValor(new_list_number))


# Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N. Por exemplo, para N = 5, o valor esperado será 15.
def funcaoSomainteiro(valor):
    soma = 0
    for numero in range(1,valor+1):
        soma += numero
    return soma

print(funcaoSomainteiro(5))

