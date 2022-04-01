#Python version 3.10.4

#Exercise 1 (write file)

def exercise1():

    name= input("Insira nome: ")
    file = open("dados.txt", "w", encoding="UTF-8-SIG")
    file.write(name)
    file.close()

#Exercise 2 
def exercise2():
    def check_name(name1,name2):
        
        pos = name1.rfind('.')#devolve a posiçao do ponto a partir da direita
        name1 = name1[0:pos] #i

        pos = name2.rfind('.')
        name1 = name2[0:pos]

        name3 = name1 + '__' + name2 + '.txt'
        return name3

    def join_file(name1, name2):
        file1 = open(name1, "r")#apontador para o ficheiro
        file2 = open(name2, "r")

        cont1, cont2 = 0

        cont1 = file1.read()#obtem conteudo e le como string
        cont2 = file2.read()

        file1.close()#fecha apontador
        file2.close()

        if cont1[-1] != '\n':
            cont1 = cont1 +'\n'

        cont3 = cont1 + cont2 #contatena as strings

        name3 = check_name(name1, name2)

        file3= open("saida.txt", "w")
        file3.write(cont3)
        file3.close()
    

    name1 = input("Insira o nome do 1º ficheiro: ")
    name2 = input("Insira o nome do 2º ficheiro: ")

    join_file(name1, name2)

#Exercise 3 
def exercise3():
    nome = input("insira o nome do 1º ficheiro: ")
    pal = input("Qual a palavra a procurar? ")

    fich = open(nome, "r")
    cont = fich.read()
    fich.close()

    qt = cont.count(pal)

    if qt == 0:
        print(f"A palavra {pal} não ocorre no ficheiro.")
    else:
        print(f"A palavra {pal} ocorre {qt} vezes no nosso ficheiro.")
'''
#Procurar palavra dada

nome = input("insira o nome do 1º ficheiro: ")
pal = input("Qual a palavra a procurar? ")
fich = open(nome, "r", encoding="UTF-8")
cont = fich.readlines() #carrega cada linha para uma lista
fich.close()
qt = 0
for frase in cont: #['Falar é fácil. Mostre-me o código. (Linus Torvalds)\n', ...]
   listfrase = frase.split() #['Falar', 'é', 'fácil.', 'Mostre-me', 'o', 'código.', '(Linus', 'Torvalds)']
   for palavra in listfrase:
      if(pal == palavra):      
         qt = qt + 1
      elif(pal in palavra) and (palavra[len(pal)] in ".,!?;:"):  
            qt = qt+1

#https://www.delftstack.com/pt/howto/python/python-count-words-in-string/
'''
#Exercise 4 
def exercise4():
    fich = open("pensamentos.txt", "r", encoding="UTF-8")
    cont = fich.read()
    fich.close()

    print(f"O conteúdo do ficheiro é:\n{cont}")

    #pedir a sequência a substituir
    seq_sai = input("Qual a sequência a remover? ")
    seq_entra = input(f"Qual a palavra a substituir {seq_sai}? ")

    cont = cont.replace(seq_sai, seq_entra)

    fich = open("pensamentos2.txt", "w", encoding="UTF-8")
    fich.write(cont)
    fich.close()

#Exercicio 5 
def exercise5():
    fich = open("pensamentos.txt", "r", encoding="UTF-8")
    cont = fich.read()
    fich.close()

    qtlinhas = cont.count('\n')
    if cont[-1] != '\n':
        qtlinhas +=1
  
    print(f"Nº de linhas: {qtlinhas}")

    listapal = cont.split()
    print(f"Nº de palavras: {len(listapal)}")

    vogais = "aeiouáàãâéêíóôõú"

    qtvog, qtcons = 0, 0
    for carater in cont:
        if carater.lower() in vogais:
      #print(f"{carater} é vogal")
            qtvog += 1
        elif 'a' < carater.lower() <= 'z' or carater.lower() == 'ç':
      #print(f"{carater} é consoante")
            qtcons += 1

    print(f"Quantidade de vogais: {qtvog}")
    print(f"Quantidade de consoantes: {qtcons}")

    cont = cont.split('\n') #conteúdo convertido em lista
    #print(cont)

    #b
    qt = 0
    numlinha = []
    pal = input("Qual a palavra a procurar? ")
    for pos, frase in enumerate(cont):
        if pal in frase:
        qt = qt + frase.count(pal)
        numlinha.append(pos+1)

    print(f"A palavra {pal} ocorre {qt} vezes nas linhas {numlinha}")

#Exercicio 6 ()
def exercise6():
    fich1 = open("fich1.txt", "r", encoding="UTF-8")
    cont1 = fich1.readlines() #['Olá mundo.\n', 'Hoje chove.\n']
    fich1.close()
    fich2 = open("fich2.txt", "r", encoding="UTF-8")
    cont2 = fich2.readlines() #['Amanhã fará sol.','Palavra.\n']
    fich2.close()
    fich3 = open("final.txt", "w", encoding="UTF-8")

    #última frase, último carater, acrescentar \n
    if cont1[-1][-1] != '\n': #'Hoje chove.\n'
        cont1[-1] = cont1[-1] + '\n'

    #1ªfrase, eliminar \n pois será a última a ser acrescentada
    if cont2[0][-1] == '\n': #'Amanhã fará sol.'
        cont2[0] = cont2[0].replace('\n','')

    #última frase, último carater, acrescentar \n
    if cont2[-1][-1] != '\n': #'Palavra.\n'
        cont2[-1] = cont2[-1] + '\n'
   
    final = cont1 + cont2[::-1] #as frases do 2º conteudo é invertido

    fich3.writelines(final)
    fich3.close()




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