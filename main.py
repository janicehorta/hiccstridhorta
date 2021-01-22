
def ValidaNome(nome):
    import re
    regex = r"[A-Z][a-z]{1,8}([a-z]{1,4}){0,1}( [A-Z][a-z]{2,8}){0,4}"
    matches = re.finditer(regex, nome, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaEmail(email):
    import re
    regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$"
    matches = re.finditer(regex, email, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaIdade(Idade):
    import re
    regex = r"[0-9]{1,3}"
    matches = re.finditer(regex, Idade, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False
def Menu(Titulo, Opcoes, np):
    print("\t\t\t\t\t\t\t\t\033[1;33;m----------------------------\033[m")
    print("\t\t\t\t\t\t\t\t\033[1;32;mPrograma do Algoritmo Tweets\033[m")
    print("\t\t\t\t\t\t\t\t\033[1;33;m----------------------------\033[m")


    from datetime import datetime
    agora = datetime.now()
    # print(agora)
    print("\033[1;30;mData: ", agora.strftime("%Y-%m-%d\033[m"))
    print("\033[1;30;mHora: ", agora.strftime("%X\033[m"))
    print("\n")
    print(Titulo)
    print()
    for i in range(np):
        print(i + 1, "- ", Opcoes[i])
    print("0 -  Terminar")
    while True:
        print("Opção?")

        op = int(input())
        if (op >= 0 and op <= np):
            break
    return op

nome_ficheiro_Tweets = "tweets.html"

def LerData(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("Data inválida")
            continue
        if data >= min and data <= max:
            break
        else:
            print("Data fora do intervalo %s e %s"
                  % (min.strftime("%Y-%m-%d"),
                     max.strftime("%Y-%m-%d")))
    return data_texto


from datetime import datetime

data_min = datetime.strptime("1000-01-01", '%Y-%m-%d')
data_max = datetime.strptime("2021-12-31", '%Y-%m-%d')





def Inserir():
    print("Inserir Tweets")

    while True:
        NomeTweets = input("Inserir Nome de Tweets")
        if ValidaNome(NomeTweets) == True:
            break
    while True:
        EmailTweets = input("Inserir Email de Tweets")
        if ValidaEmail(EmailTweets) == True:
            break
    while True:
        IdadeTweets = input("Inserir Idade de Tweets")
        if ValidaIdade(IdadeTweets) == True:
            break

    f = open(nome_ficheiro_Tweets, "at")
    print("%s" % NomeTweets, file=f, end='\t', sep='')
    print("%s" % EmailTweets, file=f, end='\t', sep='')
    print("%s" % IdadeTweets, file=f)


    input("Prima enter para continuar!")
def Alterar():
    f = open(nome_ficheiro_Tweets, "rt")
    cabecalho = f.readline()
    tweets = f.readlines()
    f.close()
    nome = input("Nome? ")
    for i in range(len(tweets)):
        j = tweets[i]
        if len(j) < 5:
            continue


        Nome, Email, Idade = j.split("\t")
        if (Nome.find(nome)) >= 0:
            # print(j)
            print("Tweets com'%s'no Nome encontrado" % nome)
            print("Nome...............: %s" % Nome)
            print("Email..............: %s" % Email)
            print("Idade..............: %s" % Idade)
            o = input("Quer alterar ?(S/N)")
            if o == "S":  # novos dados
                while True:
                    Nome = input("Inserir novo Nome do Clube?")
                    if ValidaNome(Nome) == True:
                        break
                f = open("tweets.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(tweets)):
                    if k == i:
                        print(Nome, Email, Idade,
                              sep='\t', file=f, end='')
                    else:
                        print(tweets[k], file=f, end='')
                f.close()
            elif o != 'S':
                break
    print("Fim da Alteração!")
    input("Prima enter para continuar!")

def Eliminar():
    f = open(nome_ficheiro_Tweets, "rt")
    cabecalho = f.readline()
    tweets = f.readlines()
    f.close()
    nome = input("Nome?")
    for i in range(len(tweets)):
        j = tweets[i]
        if len(j) < 3:
            continue
        # Jogador	Equipa	Posição	JJ	G
        Nome, Email, Idade = j.split("\t")
        if (Nome.find(nome)) >= 0:
            # print(j)
            print("Tweets com'%s'no Nome encontrado" % nome)
            print("Nome...............: %s" % Nome)
            print("Email..............: %s" % Email)
            print("Idade..............: %s" % Idade)
            o = input("Quer eliminar ?(S/N)")
            if o == "S":  # novos dados

                f = open("tweets.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(tweets)):
                    if k != i:
                        print(tweets[k], file=f, end='')
                f.close()
                f = open("log_tweets.txt", "at")
                print("Operação:" "eliminar" + " Tweets")
                print("\n")
                f.close()
            elif o != 'S':
                break
    print("Fim da Eliminação de Tweets!")
    input("Prima enter para continuar!")

def Listar():
    print("Listas de Todos os Tweets!")
    f = open(nome_ficheiro_Tweets, "rt")
    linhas = f.readlines()  # vector
    f.close()
    # print("\n\033[1;mListagem de todos os Clubes\n")
    print("%s %s %s" % (
        "Nome", "Email", "Idade"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Nome = colunas[0]
        Email = colunas[1]
        Idade = colunas[2]
        # Numero_Modalidades = colunas[3]
        print("%s %s %s" % (Nome, Email, Idade))
        print("")
    input("Prima enter para continuar!")

def Pesquisar():
    # pedir o nome a procurar
    # Ler o ficheiro para um vetor
    # comparar o nome de cada elemento do
    # vetor com o nome_procurar
    # nome_procurar = LerNome()
    nome_procurar = input("Nome a procurar?")
    f = open(nome_ficheiro_Tweets, "rt")
    linhas = f.readlines()  # vetor
    f.close()
    enc = False
    for linha in linhas:
        nome = linha[0:49]
        data = linha[50:50 + 10]
        if nome.find(nome_procurar) >= 0:
            print(linha)
            enc = True
    if not enc:
        print("O nome %s não existe." % nome_procurar)
    print("Fim da Pesquisa!")
    input("Prima Enter pra Continuar!")
def Contar():
    print("Contargens dos Tweets!")
    f = open(nome_ficheiro_Tweets, "rt")
    linhas = f.readlines()  # vector
    np = 0
    f.close()
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Nome = colunas[0]
        Email = colunas[1]
        Idade = colunas[2]

        np = np + 1
    print("Numero Total de Tweets %2s!" % (np))
    input("Prima enter para continuar")

def MenuPrincipal():
    print("\n")
    Titulo = "Menu Principal"
    Opcoes = ["Inserir", "Alterar", "Eliminar", "Listar", "Pesquisar", "Ordenar", "Agrupar", "Exportar"]

    np = 8
    while True:

        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            Inserir()
        elif op == 2:
            Alterar()
        elif op == 3:
            Eliminar()
        elif op == 4:
            Listar()
        elif op == 5:
            Pesquisar()
        elif op == 6:
            Contar()
        elif op == 7:
            print("Agrupar")
        elif op == 0:
            break
        break


MenuPrincipal()