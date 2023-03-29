import webbrowser
import pyautogui
from time import sleep

# Opção 1 (descomentar a opção desejada)
# telefones = [5548995853584, 554799558685, 5547558896584]
# Opção 2 (descomentar a opção desejada)
telefones = []
with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n'[0]))

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1512,208,duration=1)
    sleep(10)
    pyautogui.typewrite('Gostaria de participar do nosso evento?(digite sim, se gostaria de participar.')
    sleep(5)
    pyautogui.press('enter')