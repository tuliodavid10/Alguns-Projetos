import requests
from rich import print
from datetime import datetime
from time import sleep
import os

# de 30 em 30 segundos, verificar o preço do dolar(em relação ao real) e se o dólar estiver abaixo de um valor, enviar um sinal, caso contrário fazer nada
# https://economia.awesomeapi.com.br/json/last/USD-BRL


def enviar_imagem(links_imagens, chat_id, caption):
    token = '5739191868:AAFmcABJT837MMPONHpABdg0kR8dwonYbNk'
    for link in links_imagens:
        requests.get(
            f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')


def obter_mensagens(apenas_ultima_mensagem=False):
    update_id = None
    token = '5739191868:AAFmcABJT837MMPONH0kR8dwonYbNk'
    data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    if len(data.json()['result']) > 0:
        if apenas_ultima_mensagem == True:
            update_id = data.json()['result'][-1]['update_id']
            data = requests.get(
                f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
            print(data.json())
            print('#'*10)
        else:
            print(data.json())
            print('#'*10)


while True:
    resultado = requests.get(
        'https://economia.awesomeapi.com.br/json/last/USD-BRL')

    cotacao_atual = float(resultado.json()['USDBRL']['ask'])
    data_atual = datetime.today().strftime('%d/%m/%Y - %H:%m')
    print(cotacao_atual)
    if cotacao_atual <= 5.22:
        imagens = ['https://i.ibb.co/Csh3r3P/atencao.jpg']

        mensagem = f'💲Dólar: ${cotacao_atual}{os.linesep}🕐Data: {data_atual}{os.linesep}💳Comprar agora: www.linkdecompra.com'
        enviar_imagem(links_imagens=imagens,
                      chat_id='-1007999504', caption=mensagem)
    else:
        pass
    sleep(30)