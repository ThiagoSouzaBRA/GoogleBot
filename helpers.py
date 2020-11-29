from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import locators
import time

class bot:

    _driver = None

    def __init__(self):
        if(self._driver == None):
            self._driver = webdriver.Chrome(ChromeDriverManager().install())
            self._driver.get("https://www.google.com/")
        
    
    def close(self):
        time.sleep(5)
        print(100*"\n")
        self._driver.close()
        self._driver.quit()

    def xPath(self, xpath):
        return self._driver.find_element_by_xpath(xpath)

    def pesquisar(self, texto):
        self.xPath(locators.input_Busca).send_keys(texto)
        self.xPath(locators.input_Busca).send_keys(Keys.ENTER)

    def pesquisar_foto(self, texto, pos):
        self.xPath(locators.input_Busca).send_keys(texto)
        self.xPath(locators.input_Busca).send_keys(Keys.ENTER)
        time.sleep(1)
        self.xPath(locators.btn_buscaImagens).send_keys(Keys.ENTER)

        if(pos <= 0):
            self.xPath("(//div[@class='islrc']//img)[1]").click()
        else:
            self.xPath("(//div[@class='islrc']//img)[" + str(pos) + "]").click()




