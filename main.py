from traceback import print_tb
from chaves import *
import json
from fs import *

print("par:")
par=input()
#print('tipo')
#tipo=input()
print('valor de entrada:')
entrada = float(input())
print('mangem(usdt)')
margem=((float(input()))/entrada)
#print('gain')
#gain=input()



if verificar_a_possibilidade(tipo='long',par=par,entrada=entrada):
    
    lancar_ordem(par=par,price=entrada,margem=margem,tipo='long')

    while(1):

        while(verificar_a_possibilidade(tipo='long',par=par,entrada=entrada)):
            time.sleep(2)                                         #ficar rodando até a ordem ser executada

        print('ordem executada')
                                                

else:
    print("ja passou")