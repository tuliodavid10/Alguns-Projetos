# 1 - Navegar até o site https://www.instagram.com
import webbrowser
import pyautogui
from time import sleep

while True:
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1)
    # 2 - Entrar com meu usuário
    pyautogui.click(1539,362,duration=1)
    sleep(1)
    pyautogui.typewrite('logi')
    sleep(1)
    # 3 - Entrar com a minha senha
    pyautogui.click(1546,398,duration=1)
    sleep(1)
    pyautogui.typewrite('s')
    sleep(1)
    # 4 - Clicar em "log in"
    pyautogui.click(1567,445,duration=1)
    sleep(20)
    # 5 - Clicar em "Not now" para não salvar navegador
    pyautogui.click(1590,603,duration=1)
    sleep(20)
    # 6 - fechar janela de "salvar senha"
    pyautogui.click(1662,88,duration=1)
    sleep(1)
    # 7 - Pesquisar pela pagina'
    pyautogui.click(1526,105,duration=1)
    sleep(1)
    pyautogui.typewrite('site')
    sleep(1)
    # 8 - Entrar na página
    pyautogui.move(0,50,duration=1)
    sleep(1)
    pyautogui.click()
    sleep(20)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(1398,595,duration=1)
    sleep(10)
    # 10 - Verificar se já curti ou não aquela postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)
    # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
    if coracao is not None:
        sleep(86400)
    # 12 - Se não tiver curtido, curtir a foto
    elif coracao == None:
        pyautogui.click(1468,746,duration=1)
        sleep(5)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(1505,749,duration=1)
        sleep(3)
        pyautogui.click(1568,834,duration=1)
        sleep(1)
        pyautogui.typewrite('Gostei dessa foto!')
        sleep(5)
        pyautogui.click(1715,832,duration=1)
        # 14 - Pausar por 24 horas
        sleep(86400)