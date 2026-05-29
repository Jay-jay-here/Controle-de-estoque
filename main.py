

import os
import pyautogui as pa
import time
#declaracao das variaveis globais
opcao='0'
opcao2='0'
opcao2='0'
decicao1='0'
opcao='0'
lista_de_produtos=['pipoca','arroz','feijao','macarrão']
#declaracao das variaveis globais
def limpar_tela():
    os.system('cls') if os.name=='nt' else 'clear'
    

menu=True
ascii=r'''

                  __                                                 
  ____   _______/  |_  ____   ________ __   ____      ______ ___.__.
_/ __ \ /  ___/\   __\/  _ \ / ____/  |  \_/ __ \     \____ <   |  |
\  ___/ \___ \  |  | (  <_> < <_|  |  |  /\  ___/     |  |_> >___  |
 \___  >____  > |__|  \____/ \__   |____/  \___  > /\ |   __// ____|
     \/     \/                  |__|           \/  \/ |__|   \/     

     '''

while menu==True:
    os.system('cls')
    print(ascii)
    print('-'*90)
    print('usuario (1) ')
    print('lista de produtos (2)')
    print('carrinho (3) ')
    print("sair (4) ")
    print('-'*90)
    #menu inicial


    #easter egg!!!!!!!!
    opcao=input('')
    if opcao=='67':
      pa.FAILSAFE= False  
      pa.press('win')
      pa.write('chrome')
      time.sleep(2)
      pa.press('enter')
      time.sleep(3)
      x,y=pa.position()
      print(y,x)
      pa.move(936 , 985)
      pa.click
      time.sleep(2)
      pa.write('rick astley')
      time.sleep(2)
      time.sleep(4)
      pa.press('enter')
      pa.press('f11')
    #easter egg!!!!!!!!



    #opcao 1
    #-----------------------------------
    if opcao=="1":
      limpar_tela()
      print('informação de usuario (1)')
      voltar=input('')
    #-----------------------------------
    #opcao 1

    #opcao 2
    elif opcao=="2":
      limpar_tela()
      print('-'*30)
      print('oque deseja fazer? ')
      print('ver lista de produtos (1)')
      print('adicionar produtos (2)')
      print('-'*30)
      opcao2=input('')
      #opcao dentro da opcao 2 ver lista
    if opcao2=='1':
        print('aqui esta  a lista de produtos:')
        print('-'*90)   
        for item in lista_de_produtos:
            print(item)
        print('-'*90)
        voltar=input('digite qualquer coisa para ir ao menu')

      #opcao dentro da opcao 2 ver lista  
      #---------------------------------


    if opcao2=='2':
      limpar_tela()
      print('adicione produtos a lista de produtos')
      adicionar_produto=input('')
      lista_de_produtos.append(adicionar_produto)
      print('-'*30)
      limpar_tela()
      print('deseja remover algo da lista? y/n')
      print('lista atual:')
      for item in lista_de_produtos:
        print(item)
    decicao1=input('')

    if decicao1=='y':
        print('nomeie o produto a ser removido')
        print(lista_de_produtos)
        tirar=input('')
        lista_de_produtos.remove(tirar)
        print('lista nova')
        print(lista_de_produtos)

      #---------------------------------
      #opcao dentro da opcao 2 ver lista  
      
    #opcao 3 
    #------------------------------------
    if opcao=='3':
            limpar_tela()
            print('escolha produtos para colocar no carrinho')
            for item in lista_de_produtos:
              print(item)
            voltar=input('')

    elif opcao=='4':
            limpar_tela()
            print('Voce escolheu sair')
            break
    #-----------------------------------
    #opcao 3