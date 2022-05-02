from re import T
from symtable import Symbol
from textwrap import indent
import time
from tracemalloc import stop

from numpy import quantile
from regex import W
from chaves import *
import json
import fs

print("par:")
par=input()
#print('tipo')
#tipo=input()
print('valor de entrada:')
entrada = input()
print('mangem')
margem=input()
#print('gain')
#gain=input()



if fs.verificar_a_possibilidade(tipo='long',par=par,entrada=entrada):
    
    fs.lancar_ordem(par=par,price=entrada,margem=margem,tipo='long')
else:
    print("ja passou")