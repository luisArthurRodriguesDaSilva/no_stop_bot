from traceback import print_tb
from chaves import *
from fs import *

import json

print("par:")
par=input()
print('tipo')
tipo=input()
print('valor de entrada:')
entrada = float(input())
print('mangem(usdt)')
margem=((float(input()))/entrada)
miudo=0.001
margem=margem-(margem%miudo)
#print('gain')
#gain=input() 
if tipo=='long' :
  stop=entrada-miudo
else:
  stop=entrada+miudo

if verificar_a_possibilidade(tipo=tipo,par=par,entrada=entrada):
    while(1):
        try:
          lancar_ordem(par=par,price=entrada,margem=margem,tipo=tipo)
        except:
          ordem_de_emergencia(margem=margem,par=par,miudo=miudo,tipo=tipo)
        while(verificar_a_possibilidade(tipo=tipo,par=par,entrada=entrada) and verificar_posição(par=par)==False):
            #tempo_de_espera=0.1+(modulo((preco_atual(par=par)-entrada)/entrada))
            #print(f"tempo:{tempo_de_espera()}")
            time.sleep(1)                                         #ficar rodando até a ordem ser executada
        print('ordem executada')
        try:
          lancar_ordem_stop(margem=margem,par=par,price=stop,tipo=tipo)
        except:
          stop_de_emergencia(margem=margem,par=par,miudo=miudo,tipo=tipo)
          
        print('stop lançada')
        while(verificar_posição(par=par)): 
            time.sleep(0.1)           
            print('em posição')  
        print("saiu")                             
else:
    print("ja passou")