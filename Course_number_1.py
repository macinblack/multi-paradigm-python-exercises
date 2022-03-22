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

#Exercicio 6 (soma apenas positivos)
def exercicio6():
    soma=0
    for x in range(5):
        valor=int(input("Introduza o valor a somar:"))
        if (valor>0):
            soma=soma+valor
    print("A soma dos positivos é %s" %soma)
    
#Exercicio 7 (quantidade de pares/impares)
def exercicio7():
    par=0
    impar=0
    for x in range(5):
        valor=int(input("Introduza os valores:"))
        if (valor%2) == 0:
            par=par+1
        elif (valor%2) != 0:
            impar=impar+1
    print("O numero de pares é %s e o número de impares é %s" %(par,impar))

#Exercicio 8 (soma até pelo menos 20)
def exercicio8():
    soma=0
    valor=0
    while soma<20:
        valor=int(input("Introduza os valores até aingir pelo menos 20:"))
        soma=soma+valor
    print("O valor atingiu igual ou superior a 20")
   
#Exercicio 9 (introduzir password)
def exercicio9():
    password=0
    while password != 1234:
        password=int(input("Introduza a password:"))
        if password != 1234:
            print("A password está errada, introduza novamente.")
    print("A password está correta")


#Exercicio 10 (soma e contagem pares)
def exercicio10():
    par=0
    valor=0
    soma=0
    while (valor%2) == 0:
        valor=int(input("Introduza os valores a somar (pares):"))
        if (valor>0):
            par=par+1
            soma=soma+valor
    print("O numero de pares é %s e a soma é %s" %(par,soma))


# map the inputs to the function blocks
options = {1 : exercise1,
           2 : exercise2,
           3 : exercise3,
           4 : exercise4,
           5 : exercise5,
           6 : exercicio6,
           7 : exercicio7,
           8 : exercicio8,
           9 : exercicio9,
           10 : exercicio10,
}

num=int(input("Insert exercise number: "))
options[num]()