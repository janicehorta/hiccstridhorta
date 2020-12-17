
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
        if NomeTweets != "":
            break
    while True:
        EmailTweets = input("Inserir Email de Tweets")
        if EmailTweets != "":
            break
    while True:
        IdadeTweets = input("Inserir Idade de Tweets")
        if IdadeTweets != "":
            break

    f = open(nome_ficheiro_Tweets, "at")
    print("%s <br>" % NomeTweets, file=f, sep='\n')
    print("%s <br>" % EmailTweets, file=f, sep='\n')
    print("%s <br>" % IdadeTweets, file=f, sep='\n')


    input("Prima enter para continuar!")


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
            print("Alterar")
        elif op == 3:
            print("Eliminar")
        elif op == 4:
            print("Listar")
        elif op == 5:
            print("Pesquizar")
        elif op == 6:
            print("Ordenar")
        elif op == 7:
            print("Agrupar")
        elif op == 8:
            print("Exportar")
        elif op == 0:
            break
        break


MenuPrincipal()