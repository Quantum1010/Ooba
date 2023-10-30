from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx')
form = driver.find_element(By.XPATH,'//*[@id="cib-action-bar-main"]//div/div[2]/div/div[1]/cib-text-input')
form.send_keys('大場くんの好きな食べ物はなんですか？')
