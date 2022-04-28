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

def maior_que_preco_atual(pari,entrada):
    par=pari.upper()
    resposta = False
    for inf in bot.get_all_tickers():
        
        if (inf['symbol']==par and float(inf['price'])< entrada):
            resposta=True
            print(inf)
    print (resposta)
        
    

if __name__ == "__main__":
    while 1:
        entrada=input()
        maior_que_preco_atual('btcusdt',entrada=entrada)
    