from operator import truediv
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

def lancar_ordem(par,price,margem,tipo):
  if(tipo=='long'):
    print(par.upper())
    bot.futures_create_order(           symbol=par.upper(),
                                        side=bot.SIDE_BUY,
                                        type="STOP_MARKET",
                                        stopPrice=price,
                                        reduceOnly=False,
                                        workingType='CONTRACT_PRICE',
                                        priceProtect=False,
                                        closePosition=False,
                                        quantity=margem)
  else:
      bot.futures_create_order(           symbol=par.upper(),
                                        side=bot.SIDE_SELL,
                                        type="STOP_MARKET",
                                        stopPrice=price,
                                        reduceOnly=False,
                                        workingType='CONTRACT_PRICE',
                                        priceProtect=False,
                                        closePosition=False,
                                        quantity=margem)

def sustentar_ordem():
    while (1):
        time.sleep(3)
        if (verificar_posição()) :
            lancar_ordem()

def maior_que_preco_atual(pari,entrada):
    par=pari.upper()
    resposta = False
    for inf in bot.get_all_tickers():
        
        if (inf['symbol']==par):
            if (inf['price']< entrada):
                print(inf)
                resposta=True
            else:
                print(inf)
    return resposta
        
    

if __name__ == "__main__":
    print("par:")
    par=input()
    print('tipo')
    tipo=input()
    print('valor de entrada:')
    entrada = input()
    print('quantidade')
    quantidade=input()
    lancar_ordem(par=par,price=entrada,margem=quantidade,tipo=tipo)
    print('lançada')