# This is my first code and i am realy pround of this. Let`s go learn the best language.
def jogar ():
    import random
    print("*****************************************")
    print("          JOGO DA ADIVINHAÇÃO             ")
    print("*****************************************")
    #Declarando as variáveis:
    #----------------------------------------------------------------------------------------
    Pontuacao =1000
    Pontuacao_Nova = 1
    Numero_Certo = random.randint(1,101)
    Tentativa_atual = 1
    print("Níveis:")
    print("01 - Cabaço")
    print("02 - Meia boca")
    print("03 - Pike bbb")
    Nivel = int(input("Selecione um Nível"))
    if(Nivel == 1):
        Total_Tentativas = 20
    elif(Nivel == 2):
        Total_Tentativas = 10
    elif(Nivel == 3):
        Total_Tentativas = 5
    else:
        print("Zé, Cê tem que escolher um numero de 01 a 03 meu consagrado!!")
    #-------------------------------------------------------------------------------------------
    for Tentativa_atual in range(1,Total_Tentativas):
        print("*******************************************************************")
        print("")
        print(f'o valor certo dessa vez é {Numero_Certo} Zé. BH é Nois')
        print("Tentativa {} de {}".format(Tentativa_atual, Total_Tentativas))
        Numero_Usuario = int(input("Chute um numero de 1 a 100:"))
        #---------------------------------------------------------------------------------
        # Variáveis Resumo:
        Chute_Maior = Numero_Usuario > Numero_Certo
        Chute_Menor = Numero_Usuario < Numero_Certo
        Chute_Certo = Numero_Certo == Numero_Usuario
        print("Você escolheu o número", Numero_Usuario, sep = "_")
        #--------------------------------------------------------------------------------
        if (Numero_Usuario <1 or Numero_Usuario>100):
            print("Oops! Você deve chutar um número entre 01 e 100.")
            continue
        elif(Chute_Certo):
            print("Parabéns! você está bom de chute, resposta correta!!!")
            print( f' Sua pontuação é {Pontuacao}')
            print("FIM DE JOGO! THAKS MAN!!")
            break
        else:
            if (Chute_Maior) and (Tentativa_atual == 5):
                print("É, o chute tá ruin pai, Cê  vai sentar é na cabeeeççç :(")
                print(f'É sobre isso Zé, Cê conquisto {Pontuacao} pontos, Zé.')
            elif (Chute_Menor) and (Tentativa_atual == 5):
                print("É, o chute tá ruin pai, Cê  vai sentar é na cabeeeççç :(")
                print(f'É sobre isso Zé, Cê conquisto {Pontuacao} pontos, Zé.')
            elif (Chute_Maior):
                print("É, o chute tá ruin pai, tenta um número menor aí sô!!")
            elif(Chute_Menor):
                print("É, o chute tá ruin pai, tenta um número maior aí sô!!")

            Pontuacao = Pontuacao - abs((Chute_Certo - Numero_Usuario))
if(__name__ == "__main__"):
    jogar()