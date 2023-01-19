from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WhatsappBot:
    def __init__(self):
        self.msg = "Bom dia - Essa mensagem foi enviada! via automatização com Python "
        self.groups = ["Compartilhamento Pessoal", "Amor ❤", "Renato Maia"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        # self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

    def MsgSend(self):
        # <span dir="auto" title="PARÇAS (Nova formação)" class="_3ko75 _5h6Y_ _3Whw5">PARÇAS (Nova formação)</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        for group in self.groups:
            group = self.driver.find_element(
                by=By.XPATH, value=f"//span[@title='{group}']")
            time.sleep(2)
            group.click()

            chatBox = self.driver.find_element(
                by=By.CLASS_NAME, value='_3Uu1_')
            time.sleep(2)
            chatBox.click()
            chatBox.send_keys(self.msg)

            send = self.driver.find_element(
                by=By.XPATH, value="//span[@data-icon='send']")
            time.sleep(3)
            send.click()
            time.sleep(5)


bot = WhatsappBot()
bot.MsgSend()
