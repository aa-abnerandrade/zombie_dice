import colorama
import os
from time import sleep
import random

colorama.init()


# CABECALHO
def cabecalho():
    """
    Limpa a tela e exibe o cabeçalho do jogo.
    """

    os.system('cls') or None
    print("\033[1;30;45m========= ZOMBIE DICE =========\033[m")
    print()


# ORIENTAÇÕES
def exibir_orientacoes():
    """
    Exibe as orientações do jogo e condições de vitória e derrota. 
    Pergunta ao usuário se deseja continuar para o jogo ou se finaliza o jogo. 
    :return: Retorna String inserida pelo usuário para seguir com o jogo ou encerrar o programa.
    """

    print("Devore cérebros e desvie dos tiros. Você é um zombie. E você quer céééérebros. Mais cérebros do que os seus amigos zombies. \n"
    "Zombie Dice é pura diversão.\nUm jogo rápido e fácil para qualquer amante dos mortos vivos (e para toda a família). Os 13 dados personalizados são as suas vítimas. Tente a sorte para comer cérebros, mas cuidado um tiro de espingarda pode dar fim à sua vida de zombie. No seu turno, cada jogador agita o tubo, pega em 3 dados e, sem olhar, rola os dados. Cada um deles representa uma pobre vítima a ser atacada. Os dados vermelhos são os mais difíceis. Os verdes são os mais fáceis e os amarelos são médios.\n"
    "Os dados possuem 3 símbolos:\n"
    "--> Cérebro: Você devorou o cérebro da sua vítima\n"
    "--> Tiro: A sua vítima deu-lhe troco\n" 
    "--> Pegadas: A sua vítima escapou\n"
    "Se você sortear 3 Tiros, já era. Mas você pode desistir antes. De um jeito ou outro o seu turno termina e é a vez do próximo jogador, e assim segue a partida. \n"
    "O jogo termina quando alguém conseguir comer 13 cérebros.")

    sleep(3)
    go_to_game = str(input("\n \033[1;35;40mE aí, vai encarar? [S/N]: \033[m")).upper()
    return go_to_game


# QUANTIDADE DE JOGADORES
def definir_qtd_players(qtd_players, confirma__qtd_players):

    while (confirma__qtd_players != "S"):
        try:
            qtd_players = int(input(":> Quantas pessoas jogarão? ")) # Mínimo 2 jogadores
            if (qtd_players < 2):
                print("\033[1;37;47m => Para jogar é necessário 2 ou mais jogadores. \033[m\n")
                continue
        except:
            print("Valor inválido")
            continue

        confirma__qtd_players = str(input(f"\nShow! Teremos {qtd_players} jogadores. \033[1;30;42mConfirma?\033[m [S/N]:  ")).upper()
        if (confirma__qtd_players == "N"):
            #print("Enviar user para Redefinir quantidade de jogadores")  # Redefinir quantidade de jogadores
            cabecalho()
            continue
        elif (confirma__qtd_players not in "NS"):
            while (confirma__qtd_players not in "NS"):
                confirma__qtd_players = str(input(f"Por favor, confirme {qtd_players} jogadores utilizando S ou N: ")).upper()
        else:
            return qtd_players


# NOMEAR JOGADORES
def nomear_players(qtd_players):
    print(f"\n\nBeleza! Teremos {qtd_players} jogadores. \nAgora identifique os jogadores.\n")
    cont = 1
    confirma__nome_players = "N"
    while (confirma__nome_players != "S"):
        nomes_players = []

        for cont in range(1, qtd_players+1):
            nome = str(input(f':> Nick do {cont}° jogador: ')).upper()
            nomes_players.append(nome)
        #print(nome_players) # Print de Teste


        print(f"\nJogadores: ") # Exbindo nicks dos jogadores
        for cont in range(0, qtd_players):
            print(f"{nomes_players[cont]:>15}")

        confirma__nome_players = str(input("\033[1;30;42mConfirma?\033[m [S/N]: ")).upper() # confirmação dos nicks de jogadores
        if (confirma__nome_players == "N"):
            #print(" Enviar para Redefinir nick de jogadores") #Redefinir nick de jogadores
            print()
            continue
        elif (confirma__nome_players != "S" and confirma__nome_players != "N"):
            while (confirma__nome_players != "S" and confirma__nome_players != "N"):
                #print("Outros caracteres") # Print de Teste
                confirma__nome_players = str(input(f"Confirma nicks dos jogadores? [S/N] ")).upper()
                continue
        elif (confirma__nome_players == "S"):
            #print("Enviar para jogo") # Continua para Jogo
            break
    return nomes_players    


#SORTEAR PLAYERS
def sortear_jogadores(nomes_players):
    print("\n\033[1;33mSorteando jogadores...\033[m")
    sleep(1)
    ordem_players = nomes_players
    random.shuffle(ordem_players)
    #print(ordem_players)
    return ordem_players

