from chaves import *
import json
import time

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
  elif tipo=='short':
      bot.futures_create_order(           symbol=par.upper(),
                                        side=bot.SIDE_SELL,
                                        type="STOP_MARKET",
                                        stopPrice=price,
                                        reduceOnly=False,
                                        workingType='CONTRACT_PRICE',
                                        priceProtect=False,
                                        closePosition=False,
                                        quantity=margem)
  print('-----------------lançou uma--------------------')

def lancar_ordem_stop(margem,par,price):#tipo):
    bot.futures_create_order(
        symbol=par.upper(),
        side=bot.SIDE_SELL,
        type="STOP_MARKET",
        stopPrice=price,
        workingType='CONTRACT_PRICE',
        priceProtect=True,
        closePosition=True,
        quantity=margem
                                        )

def sustentar_ordem():
    while (1):
        time.sleep(3)
        if (verificar_posição()) :
            lancar_ordem()

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
        print("em long")
        return(maior_que_preco_atual(pari=par,entrada=entrada))
    elif (tipo == 'short'):
        print("em short")
        return(maior_que_preco_atual(pari=par,entrada=entrada)==False)

    

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