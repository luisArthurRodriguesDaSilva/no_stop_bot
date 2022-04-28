from re import T
from symtable import Symbol
from textwrap import indent
import time

from numpy import quantile
from chaves import *
import binance
import json

secret_key=chavess["secretKey"]
api_key=chavess['apiKey']

bot = binance.Client(api_key,secret_key)

def verificar_posição(par):
    for posicao in bot.futures_position_information():
        if(posicao['symbol'] ==f'{par.upper()}'):
            if(posicao['entryPrice'] != '0.0'):
                return True
            else:
                return False

def lancar_outra_ordem():
    bot.futures_create_order(
         
    )
def sustentar_ordem():
    while (1):
        time.sleep(3)
        if (verificar_posição()) :
            lancar_outra_ordem()



while 1 :
    par=input()
    print(verificar_posição(par=par))