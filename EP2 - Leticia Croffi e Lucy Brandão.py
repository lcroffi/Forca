#Turma A - ADS - 1º semestre
#Leticia Brum Croffi
#Lucy Brandão
#Python version: 3.6.1

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

def escolhe():
       if lista == []:
              html = urlopen("https://www.dicionariodenomesproprios.com.br/top-brasil/")
              bsObj = BeautifulSoup(html.read(), "html.parser")
              nameList = bsObj.findAll("li")
              for name in nameList:
                  if '<span>' in str(name):
                      lista.append(name.find('a').get_text())
       escolha = random.choice(lista)
       escolha = sem_acentos(escolha)
       return escolha.lower()

def sem_acentos(escolha):
       escolha = escolha.replace('í','i').replace('ú','u').replace('ã','a')
       escolha = escolha.replace('é','e').replace('ô','o').replace(' ','')
       return escolha

def desenha(erro):
       forca = ['''
 _______
|/      |
|       0
|      /|\\
|       |
|    _/  \\_ 
|
|___''','''
 _______
|/      |
|       0
|      /|\\
|       |
|      / \\_ 
|
|___''','''
 _______
|/      |
|       0
|      /|\\
|       |
|      / \\
|
|___''','''
 _______
|/      |
|       0
|      /|\\
|       |
|        \\
|
|___''','''
 _______
|/      |
|       0
|      /|\\
|       |
|
|
|___''','''
 _______
|/      |
|       0
|       |\\
|       |
|
|
|___''','''
 _______
|/      |
|       0
|       |
|       |
|
|
|___''','''
 _______
|/      |
|       0
|       |
|
|
|
|___''','''
 _______
|/      |
|       0
|
|
|
|
|___''','''
 _______
|/      |
|
|
|
|
|
|___''']
       print (forca[erro],'\n')
       for c in escolha:
              if c in certas:
                     print (c.upper(), end=' ')
              else:
                     print ('_', end=' ')

def chute(letras):
       while not re.match("^[A-Za-z]*$", letras):
              letras = input('Apenas letras: ')
       while len(letras) != 1:
              letras = input('Apenas uma letra: ')
       while verifica(letras):
              letras = input('Essa já foi, tente outra: ')
       return letras.lower()

def verifica(letras):
       for c in certas:
              if c == letras:
                     return True
       for c in erradas:
              if c == letras:
                     return True
       else:
              return False
    
def jogar_novamente():
       resposta = input('Deseja jogar novamente? S/N ')
       if resposta.lower() == 'n':
              return False
       elif resposta.lower() == 's':
              return Jogo()
       else:
              resposta = input('Digite uma resposta válida. S/N ')             

def ganhou():
       if sorted(set(escolha)) == sorted(set(certas)):
              return True
       else:
              return False

def Jogo():
    global certas
    global erradas
    global erro
    global escolha
    global lista
    letras = ''
    letra = ''
    escolha = ''
    certas = ''
    erradas = ''
    erro = 9
    escolha = escolhe()
    desenha (9)
    while True:
        letras = input('\nChute uma letra: ')
        letra = chute(letras)
        if letra in escolha:
            certas = certas + letra
            desenha(erro)
            if ganhou():
                    print ('\nParabéns! Você venceu!')
                    if not jogar_novamente():
                        break
        else:
            erradas = erradas + letra
            erro -= 1
            desenha(erro)
        if erro == 0:
                  print ('\nVocê perdeu...')
                  if not jogar_novamente():
                      break

lista = []
Jogo()
