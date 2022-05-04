from traceback import print_tb
from chaves import *
import json
from fs import *

print("par:")
par=input()
#print('tipo')
#tipo=input()
tipo='long'
print('valor de entrada:')
entrada = float(input())
print('mangem(usdt)')
margem=((float(input()))/entrada)
margem=margem-(margem%0.001)
#print('gain')
#gain=input()
stop=entrada*0.999



if verificar_a_possibilidade(tipo='long',par=par,entrada=entrada):
    
    lancar_ordem(par=par,price=entrada,margem=margem,tipo=tipo)

    while(1):

        while(verificar_a_possibilidade(tipo='long',par=par,entrada=entrada)):
            time.sleep(5)                                         #ficar rodando até a ordem ser executada

        print('ordem executada')
        lancar_ordem_stop(margem=margem,par=par,price=stop)
        print('stop lançada')
        while(verificar_posição(par=par)):            
            print('em posição')                               
              
else:
    print("ja passou")