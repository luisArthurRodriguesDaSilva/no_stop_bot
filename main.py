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


while 1:
    entrada=input()
    if fs.verificar_a_possibilidade(tipo='long',par='btcusdt',entrada=entrada):
        print("ta maior")
    else:
        print('ta menor')