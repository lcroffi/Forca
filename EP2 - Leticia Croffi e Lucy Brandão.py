#Turma A - ADS - 1º semestre
#Leticia Brum Croffi
#Lucy Brandão

lista = []

def escolhe():
       if lista == []:       
              from urllib.request import urlopen
              from bs4 import BeautifulSoup

              html = urlopen("https://www.dicionariodenomesproprios.com.br/top-brasil/")
              bsObj = BeautifulSoup(html.read(), "html.parser")
              nameList = bsObj.findAll("li")
              for name in nameList:
                  if '<span>' in str(name):
                      lista.append(name.find('a').get_text())
       import random
       escolha = random.choice(lista)
       return escolha



def desenha(erro):
       forca = ['''
 _______
|/      |
|       0
|      /|\
|       |
|    _/  \_ 
|
|___''','''
 _______
|/      |
|       0
|      /|\
|       |
|      / \_ 
|
|___''','''
 _______
|/      |
|       0
|      /|\
|       |
|      / \
|
|___''','''
 _______
|/      |
|       0
|      /|\
|       |
|        \
|
|___''','''
 _______
|/      |
|       0
|      /|\
|       |
|
|
|___''','''
 _______
|/      |
|       0
|       |\
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



def chute(letras):
    

def jogar_novamente():


def ganhou():
