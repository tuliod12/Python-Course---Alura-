# This is my second python  code and i am realy pround of this. Let`s go learn the best language.
import random
def Jogar():
    enforcou = False
    acertou = False

    menu()
    Arquivo_Defeitos = open("Defeitos.txt", "r")
    Lista_Defeitos = []
    for i in Arquivo_Defeitos:
        Novo_Defeito = i
        Novo_Defeito = Novo_Defeito.strip()
        Lista_Defeitos.append(Novo_Defeito)
    Arquivo_Defeitos.close()
    Indice = random.randrange(0,len(Lista_Defeitos))
    Magic_Word = Lista_Defeitos[Indice]
    print(Magic_Word)
    Lista_Magic_Word = list(Magic_Word.upper())
    Palavra_Instantanea = ["_" for j in Magic_Word]
    erro: int = 0
    tentativas = 6

    while (not enforcou and not acertou):
        Index = 0
        if (Lista_Magic_Word == Palavra_Instantanea):
            print("Voce acertou")
            break
        else:
            print("write the the magic word please guy:")
            User_letter = str(input("Go, input here the letter you think makes part of the the magic word:"))
            User_letter = User_letter.strip().upper()
            if (User_letter in Magic_Word.upper()):
                for i in Magic_Word:
                    if (i.upper() == User_letter.upper()):
                        print(f'Man the letter {User_letter} that you choosen is on the position {Index} of the magic word')
                        Palavra_Instantanea[Index] = User_letter
                    Index = Index + 1
                print(Palavra_Instantanea)
                print(f'a lista certa: {Lista_Magic_Word}')
            else:
                erro += 1
                tentativas -= 1
                print("é pai, tem essa letra nao viu")
                print(f'Cê inda tem {tentativas} tentativas zé')
            if (erro == 6):
                print("cabô suas chance cabaçãooo!!!")
                print("GAME OVER!!!! HAHAHAHAHAHAH")
                enforcou = True
            else:

                if(enforcou != True):
                    print("*****************************************************")
                    print("                  TRY AGAIN                          ")
                    print("*****************************************************")


# Funcoes:
def menu():
    print("*****************************************")
    print("         HANGMAN GAME            ")
    print("*****************************************")

if (__name__ == "__main__"):
    Jogar()
