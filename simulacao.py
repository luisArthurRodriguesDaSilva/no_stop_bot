import time
from fs import *
from numpy import quantile
from chaves import *
import binance
import json

while 1 :
    
    print("par:")
    par=input()
    print('valor de entrada:')
    entrada = input()
    print('gain')
    gain=input()

    valor_do_stop = entrada-(entrada/1000)

 