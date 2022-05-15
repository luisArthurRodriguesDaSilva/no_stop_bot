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
margem=margem-(margem%0.01)
#print('gain')
#gain=input() 
stop=entrada-0.01


tempo_de_espera=lambda : 0.1+(module((preco_atual(par=par)-entrada)/entrada))
if verificar_a_possibilidade(tipo='long',par=par,entrada=entrada):
    
    while(1):
        lancar_ordem(par=par,price=entrada,margem=margem,tipo=tipo)

        while(verificar_a_possibilidade(tipo='long',par=par,entrada=entrada) and verificar_posição==False):
            
            print(f"tempo:{tempo_de_espera()}")
            time.sleep(1)                                         #ficar rodando até a ordem ser executada

        print('ordem executada')
        lancar_ordem_stop(margem=margem,par=par,price=stop)
        print('stop lançada')
        while(verificar_posição(par=par)): 
            time.sleep(0.1)           
            print('em posição')                               
              
else:
    print("ja passou")