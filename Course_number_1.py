#Python version 3.10.2

#Exercise 1 (count chars with tuples)

from time import process_time_ns


def exercise1():
    def calculate(phrase):
        qtm,qtM,qtd=0,0,0

        for symbol in phrase:
            if symbol.islower():
                qtm = qtm + 1
            elif symbol.isupper():
                qtM = qtM + 1
            elif '0' <= symbol <= '9':
                qtd= qtd + 1

        return(qtm,qtM,qtd)
 

    phrase=input("Insira a frase: ")
    ans=calculate(phrase) 
    print(f"Quantidade de minúsculas: {ans[0]}")
    print(f"Quantidade de maiúsculas: {ans[1]}")
    print(f"Quantidade de digitos: {ans[2]}") # fix



#Exercise 2 
def exercise2():
    tuple = ()
    count = 10
    while count > 0:
        n = int(input("Insert 1 number: "))
        tuple = tuple + (n,) # turn n in tuple class
        count-= 1
    print(tuple)

#Exercise 3 
def exercise3():
    t1 = (2,5,3)
    t2 = (5,0,2)
    t3 = ()

    qt = len(t1)
    i=0
    while i < qt:
        sum=t1[i] + t2[i] # 2 + 5 
        t3 = t3 + (sum,) # (7,5)
        i+=1

#Exercise 4 
def exercise4():
    def convert(list):
        return tuple(i for i in list)

    def str_comuns(st1,st2):
        len_s1= len(st1)
        len_s2= len(st2)
        result =[]
        for a in range(len_s1):
            for b in range(a+1,len_s2):
                if st1[a]==st2[b]:
                    result.append(st1[a])
        return convert(result)


    r = str_comuns("2Luis","22tLuisattt")
    print(r)

#Exercicio 5 (Numeros primos)
def exercise5():
    def ver_primo(t):
        primo = () # guardar os numeros primos que encontrar
        
        for elem in t:
            qtdiv = 0
            x=1

            while x <= elem:
                if ((elem %x)==0): #x e o divisor
                    qtdiv +=1
            if qtdiv ==2: # se tiver 2 entao guarda o elem no tuplo do primos
                primo = primo + (elem,) # concatenar tuplos
        return primo

    tuplo = (9,3,7,199,6,11)
    resp = ver_primo(tuplo) #tuplo (n1, n2, ... ,nn)

    if len(resp) > 0:
        print(f"Do tuplo inicial {resp} os primos são {resp}")
    else:
        print(f"Não existem elementos primos no tuplo {tuplo}")

#Exercicio 6 ()
def exercise6():
    def substituir (tuplo, sai, entra):
        t=()
        for elem in tuplo:
            if elem != sai:
                t= t + (elem,)
            else:
                t = t +(entra,)
        return t
    
    
    tuplo = (9,3,7,199,6,11)
    print (f"Tuplo -> {tuplo}")
    sai = int(input("qual o valor a substituir? "))
    entra = int(input(f"Qual o valor que ira susbtituir? "))

    resp= substituir(tuplo,sai, entra)
    print(f"o tuplo resultante é {tuplo}")

#Exercicio 7 ()
def exercise7():
    cidades = []

    for x in range(5):
        nome = input("indique o nome de uma cidade: ")
        cidades = cidades + [nome] #cidades.append(nome)
    
    print("as cidades inseridas foram: {cidades}")

#Exercicio 8 ()
def exercise8():
    def remover (cidades):
        delete = input(f"Das seguintes cidades, qual deseja remover? {cidades}")
        if delete not in cidades:
            print(f"Não foi possivel remover {delete}")
        else:
            cidades.remove(delete)
            print(f"A nova lista é {cidades}")
    
    cidades = ['Porto', 'Braga', 'Aveiro']
    remover(cidades)
   
#Exercicio 9 ()
def exercise9():
    def trocar(cidades, sai, entra):
        i=0
        while i < len(cidades):
            if cidades[i] == sai:
                cidades[i] = entra
                return cidades
            i += 1
        return f"Não foi possivel substituir {sai} por {entra}"

    cidades = ['Porto', 'Braga', 'Aveiro']
    print(f"Cidades disponiveis: {cidades}")
    sai = input("Qual a cidade que deseja substituir? ").title().strip()
    entra = input(f"Qual a cidade que substitui {sai} ").title().strip()

    novalista = trocar(cidades, sai, entra)
    print(f"A lista de cidades resultante é {novalista}")

#Exercicio 10 (include 10, 11 and 12 exercise all in one)
def exercise10():
    fruits = ['Laranja', 'Banana', 'Morango', 'Pera', 'Pessego']
    qt = len(fruits)
    print(f"Existem {qt} espécies de frutos registados, sendo eles: ")
    for fruit in fruits:
        print(fruit)
    
    new = input("Adicione um novo fruto: ")
    if new not in fruits: # se ainda nao existir na lista o fruto novo
        fruits.append(new)
    
    for fruit in fruits:
        print(fruit)

#Exercicio 11 ()
def exercise11():
    fruits = ['Laranja', 'Banana', 'Morango', 'Pera', 'Pessego']
    rem = input("Qual o fruto que deseja remover da lista? ")
    if rem not in fruits:
        print(f"Não é possive remover o fruto {rem} da lista {fruits}")
    else:
        for f in fruits:
            print("Peguei na peça {f}")
            input()
            if f == rem:
                fruits.remove(rem)
                print(fruits, f)


# map the inputs to the function blocks
options = {1 : exercise1,
           2 : exercise2,
           3 : exercise3,
           4 : exercise4,
           5 : exercise5,
           6 : exercise6,
           7 : exercise7,
           8 : exercise8,
           9 : exercise9,
           10 : exercise10,
           11: exercise11,
}

num=int(input("Insira o número do exercicio: "))
options[num]()