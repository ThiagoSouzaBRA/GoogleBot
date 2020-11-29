## https://github.com/ThiagoSouzaBRA
## Thiago Souza

import helpers
import time

#Selecionando operação
print("O que deseja fazer ?")
print("/texto - Pesquisa simples.")
print("/foto - Pesquisar Foto.")
op = input("Digite a operação:\n")

if(op.lower() == '/texto'):    
        txt = input("Por favor digite o texto que deseja pesquisar:\n")
        #Pesquisar somente.
        _bot = helpers.bot()
        _bot.pesquisar(txt)
elif(op.lower() == '/foto'):
        txt = input("Por favor digite a foto que deseja pesquisar:\n")
        #Pesquisar por foto
        _bot = helpers.bot()
        _bot.pesquisar_foto(txt, 1)


_bot.close()