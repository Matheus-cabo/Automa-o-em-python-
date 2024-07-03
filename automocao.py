import pandas as pd 
import pyautogui 
import time 

#Iniciar a automação 
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
time.sleep(4)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
pyautogui.click(x=582, y=252)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
tabela = pd.read_csv("alunos.csv")
for linha in tabela.index:
    pyautogui.click(x=463, y=332)
    nome = tabela.loc[linha,"Nome"]
    pyautogui.write(str(nome))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"Email"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"Endereco"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"Telefone"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.scroll(5000)

