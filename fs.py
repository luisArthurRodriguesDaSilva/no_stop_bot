from chaves import *

import json
import time

def stop_de_emergencia(margem,par,miudo,tipo):
    for inf in bot.futures_mark_price():
   
        if (inf['symbol']==par):
            preco_atual=float(str(inf['markPrice']))
   
    if(tipo == 'long'):
        variante=bot.SIDE_SELL
    elif(tipo=='short'):
        variante=bot.SIDE_BUY
   
    time.sleep(0.2)
    bot.futures_create_order(
        symbol=par.upper(),
        side=variante,
        type="MARKET",
        workingType='CONTRACT_PRICE',
        priceProtect=True,
        closePosition=False,
        quantity=margem
    )
    print("________________passei pelo stop de emergencia____________________________")
def ordem_de_emergencia(margem,par,miudo,tipo):
    for inf in bot.futures_mark_price():
   
        if (inf['symbol']==par):
            preco_atual=float(str(inf['markPrice']))
   
    if(tipo == 'long'):
        variante=bot.SIDE_BUY
    elif(tipo=='short'):
        variante=bot.SIDE_SELL
   
    time.sleep(0.2)
    bot.futures_create_order(
        symbol=par.upper(),
        side=variante,
        type="MARKET",
        workingType='CONTRACT_PRICE',
        priceProtect=False,
        closePosition=False,
        quantity=margem
    )
    print("________________passei pela ordem de emergencia____________________________")

def remover_espaco(word1):
    word2 = ' '
    for i in word2:
        word1 = word1.replace(i, '')
    return(str(word1))

def verificar_posição(par):
    for posicao in bot.futures_position_information():
        if(posicao['symbol'] ==f'{par.upper()}'):
            if(posicao['entryPrice'] != '0.0'):
                return True
            else:
                return False

def lancar_ordem(par,price,margem,tipo):
    if(tipo == 'long'):
        variante=bot.SIDE_BUY
    elif(tipo=='short'):
        variante=bot.SIDE_SELL
    print(par.upper())
    bot.futures_create_order(           symbol=par.upper(),
                                        side=variante,
                                        type="STOP_MARKET",
                                        stopPrice=price,
                                        reduceOnly=False,
                                        workingType='CONTRACT_PRICE',
                                        priceProtect=False,
                                        closePosition=False,
                                        quantity=margem)

    print('-----------------lançou uma--------------------')

def lancar_ordem_stop(margem,par,price,tipo):
    if(tipo == 'long'):
        variante=bot.SIDE_SELL
    elif(tipo=='short'):
        variante=bot.SIDE_BUY
    bot.futures_create_order(
        symbol=par.upper(),
        side=variante,
        type="STOP_MARKET",
        stopPrice=price,
        workingType='CONTRACT_PRICE',
        priceProtect=True,
        closePosition=True,
        quantity=margem
                                        )
    print("lançou stop")

def modulo(x): 
    if(x<0):
        x=-x
    return x

def preco_atual(par):
    valor=1
    for inf in bot.futures_mark_price():
        if (inf['symbol']==par):
            valor=float(str(inf['markPrice']))
    return valor

def maior_que_preco_atual(pari,entrada):
    par=pari.upper()
    for inf in bot.futures_mark_price():

       if (inf['symbol']==par):
            valor=float(str(inf['markPrice']))
        
            print(f"valor={valor}aaaaa{type(valor)}")
            if (valor < float(entrada)):
                print(inf)
                resposta=True
            else:
                print(inf)
                resposta=False
    return resposta

    
def verificar_a_possibilidade(tipo,par,entrada):
    if (tipo =='long') :
        #print("em long")
        return(maior_que_preco_atual(pari=par,entrada=entrada))
    elif (tipo == 'short'):
        #print("em short")
        return(maior_que_preco_atual(pari=par,entrada=entrada)==False)

    

