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
print('tipo')
tipo=input()
print('valor de entrada:')
entrada = input()
print('quantidade')
quantidade=input()
print('gain')
gain=input()

while 1:
    entrada=input()
    if fs.verificar_a_possibilidade(tipo=tipo,par=par,entrada=entrada):
        print("passou")
    else:
        print('n passou')