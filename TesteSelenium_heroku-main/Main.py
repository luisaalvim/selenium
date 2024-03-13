from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path ='C:\\Users\\LabInfo\\Documents\\teste.2\\TesteSelenium_heroku-main\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://the-internet.herokuapp.com/key_presses?")
    

    def enviarDados(teste):
       
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "target"))
        )
        
        btn_login.send_keys(teste)
        driver.implicitly_wait(5)  
        alert = driver.find_element(By.ID, "result").text
        return alert
        
    
    alert = enviarDados('C')
    if 'You entered: C' in alert :
        print("Teste bem sucedido")
    else:
        print("Teste falhou")
        
    
    alert = enviarDados('M')
    if 'You entered: M' in alert:
        print("Teste bem sucedido")
    else:
        print("Teste falhou")
        
  
    alert = enviarDados(Keys.Space)
    if 'You entered: SPACE' in alert:
        print("Teste bem sucedido")
    else:
        print("Teste falhou")
        

    alert = enviarDados(Keys.F5)
    if 'You entered: F5' in alert:
        print("Teste bem sucedido")
    else:
        print("Teste falhou")

    print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()