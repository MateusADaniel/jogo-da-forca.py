palavras = ["casa", "fogo", "amor", "solto","azul", "perto","lagoa","chuva","gato","frio", "amoroso","banheiro","caminho","desejar","camisa","humilde","jardim","piscina","trabalho","universo"
            "universidade","refrigerador","sustentabilidade","desenvolvimento","arquitetura","internacional","reconhecimento","impressionante","sobrenatural","desinteressado"]

import random
import pickle

with open("banco_de_palavras.pkl", "wb") as arquivo:

    pickle.dump(palavras, arquivo)

arquivo.close()

# Abrir o arquivo com o banco de palavras
with open("banco_de_palavras.pkl", "rb") as arquivo:
    banco_de_palavras = pickle.load(arquivo)

# Escolher uma palavra aleatoriamente
palavra_aleatoria = random.choice(banco_de_palavras)

# Separa as palavras por nível de dificuldade
palavras_fácil = [p for p in palavras if 4 <= len(p) <= 5]
palavras_médio = [p for p in palavras if 6 <= len(p) <= 10]
palavras_difícil = [p for p in palavras if len(p) > 10 or " " in p]

#######################################################

print("                                        **** JOGO DA FORCA****")
print("          ")
print("REGRAS DO JOGO: ")
print("1- O número de tentativas permitidas para o usuário deve ser proporcional ao tamanho da palavra")
print("2- O jogo é dividido em 3 níveis de dificuldade: ")
print("                                                Fácil: Palavras de 4 a 5 letras")
print("                                                Médio: Palavras de 6 a 10 letras")
print("                                                Difícil: Palavras maiores que 10 letras ou “Frases Conhecidas")
print("3- O boneco só possui 6 membros, então para palavras maiores será necessário mais erros para contar um membro.")
print("          ")
print("--------------------------------------------------------------------------------------------------------------------")
print("          ")

# Pergunta ao usuário qual é o nível de dificuldade desejado
nivel = input("Escolha o nível de dificuldade (Fácil, Médio ou Difícil): ").lower()
print("          ")
print("          ")
# Separar por nivel (SO UMA IDEIA)
if nivel == "fácil":
    palavra = random.choice(palavras_fácil)
elif nivel == "médio":
    palavra = random.choice(palavras_médio)
else:
    palavra = random.choice(palavras_difícil)


##############################################################################


print(palavra)
#contar tamanho do palavra e definir o numero de tentativas
letter = [x for x in palavra]
tam = len(letter)
print("A palavra tem {} letras, logo possui {} tentativas.".format(tam,tam))
#aparecer o o local onde vai as letras
vazia = []
i=0

#comece os jogos

print("   +---+ ")
print("   |   | ")
print("       | ")
print("       | ")
print("       | ")
print("       | ")
print("_______| ")
print("         ")

while(i<tam):
  vazia.append('_')
  i+=1

n_erros = 0
tentativa = 0
#while de entrada e saida do jogo, conta os erros
letras_digitadas = []
print(vazia)
while True:

  tentativa = tentativa + 1
  letra = input('Digite uma letra: ')
  letras_digitadas.append(letra)

  i = 0
  flag_entrei = 0
  
  #Verifica se a letra digitada
  #Existe no vetor letras
  while(i<tam): 

    if (letter[i] == letra):   
      vazia[i] = letra
      flag_entrei = 1     
    
    i+=1
    
  if flag_entrei == 0:
    n_erros += 1


    if tam == 4 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")
    
    
    if tam == 5 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")


    if tam == 6 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")
  

    if tam == 7 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")


    if tam == 8 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")

    if tam == 11 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 9 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 10 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 11:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")
    if tam == 12 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 9 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 10 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 11 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 12:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")
    if tam == 13 :
      if n_erros == 1:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 9:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 10 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 11 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 12 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 13:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")

    if tam == 14 :
      if n_erros == 1:  
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 9 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 10:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 11 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 12 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 13 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 14:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")
    if tam == 15 :
      if n_erros == 1:  
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 9:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 10 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 11:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 12 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 13 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 14 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 15 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")
    if tam == 16 :
      if n_erros == 1:  
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 2:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 3:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("       | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 4:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 5:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 6:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("   |   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 7:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 8:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 9:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|   | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 10:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 11 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 12:
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("       | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 13 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 14 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 15 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  /    | ")
        print("       | ")
        print("_______| ")
      elif n_erros == 16 :
        print("   +---+ ")
        print("   |   | ")
        print("   O   | ")
        print("  /|\  | ")
        print("  / \  | ")
        print("       | ")
        print("_______| ")



  print(vazia)
  print("Erros: ",n_erros)

# verificar se todas as letras da palavra foram adivinhadas
  palavra_adivinhada = True
  for letra_palavra in palavra:
      if letra_palavra not in letras_digitadas:
          palavra_adivinhada = False
          break
  
  if palavra_adivinhada:
      print("Parabéns, você acertou!")
      break
  
  if tentativa > tam :
    print("Você Perdeu! Acabaram as suas chances!")
    break
