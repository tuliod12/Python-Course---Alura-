# This is my first code and i am realy pround of this. Let`s go learn the best language.
import Jogo_Forca
import Jogo_Adivinhacao
print("*****************************************")
print("          ZÉ, ESCOLHE O GAME AÍ ZÉ:            ")
print("*****************************************")
print("")
print("1 - Jogo da adivinhação ")
print("2 - Jogo da forca")
Escolhido = int(input("Escolha uma das opções acima:"))

if(Escolhido == 1):
    print("Você escolheu o jogo da adivinhação")
    Jogo_Adivinhacao.jogar()
elif(Escolhido == 2):
    print("Você escolheu o jogo da forca")

    Jogo_Forca.Jogar()
else:
    print("Escolha um jogo dentro das opções carai!!")


