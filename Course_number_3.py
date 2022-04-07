
def exercise1():
#Ex1
#dados guardados no ficheiro dados.csv
#Ana,Lisboa,22,Centro
#Pedro,Porto,45,Norte
#Isabel,Coimbra,22,Centro

    def elimina(cont):
   #cont=[ "Ana,Lisboa,22,Centro\n", "Pedro,Porto,45,Norte\n", ... ]
        for ind, frase in enumerate(cont):
        novafrase = frase.replace('\n', '')
        cont[ind] = novafrase

        return cont

    fich = open("dados.csv", "r", encoding="UTF-8-SIG")
    cont = fich.readlines()
    fich.close()

    #eliminar '\n' de todas as frases
    cont = elimina(cont)

    #a
    num_pessoas = len(cont)
    print(f"Estão registadas {num_pessoas} pessoas no ficheiro.")

    #b Qts pessoas por zonas
    #cont=['Ana,Lisboa,22,Centro','Pedro,Porto,45,Norte', ... ]

    qtN, qtC, qtS = 0,0,0
    for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
        dados = pessoa.split(',') #dados = ['Ana','Lisboa','22','Centro']
        zona = dados[3]
        if zona == 'Norte':
            qtN += 1
        elif zona == 'Centro':
            qtC += 1
        else:
            qtS += 1

    print(f"Quantidade de pessoas do norte: {qtN}")
    print(f"Quantidade de pessoas do centro: {qtC}")
    print(f"Quantidade de pessoas do sul: {qtS}")






# map the inputs to the function blocks
options = {1 : exercise1,
           2 : exercise2,
           3 : exercise3,
           4 : exercise4,
           5 : exercise5,
           6 : exercise6,
}

num=int(input("Insira o número do exercicio: "))
options[num]()