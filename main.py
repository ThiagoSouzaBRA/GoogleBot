## https://github.com/ThiagoSouzaBRA
## Thiago Souza

import helpers
import time

#Selecionando operação
print("O que deseja fazer ?")
print("/texto <TEXTO> - Pesquisar um simples.")
print("/foto  <TEXTO> - Pesquisar Foto por texto.")
op = input("Digite a operação:\n")

if(op.split(" ")[0] == '/texto'):
        #Pesquisar somente.
        _bot = helpers.bot()
        _bot.pesquisar(op.split(" ")[1])
elif(op.split(" ")[0] == '/foto'):
        #Pesquisar por foto
        _bot = helpers.bot()
        _bot.pesquisar_foto(op.split(" ")[1], 1)


_bot.close()