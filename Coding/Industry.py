from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time


driver=webdriver.Firefox()
driver.get('https://it.finance.yahoo.com/quote/AAPL/profile?p=AAPL')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html.ltr.yahoo-page.height100 body#tcf2-layer1.no-touch.blur-preview-tpl.wizard.tcf-2.yahoo.eu-localized.it-IT.js div#consent-page.theme-2.v4.brandtype-yahoo div.consent-overlay div.container.con-container.is-reject-all-enabled div.con-wizard div.scroll-down-wrapper.show button#scroll-down-btn.btn"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html.ltr.yahoo-page.height100 body#tcf2-layer1.no-touch.blur-preview-tpl.wizard.tcf-2.yahoo.eu-localized.it-IT.js div#consent-page.theme-2.v4.brandtype-yahoo div.consent-overlay div.container.con-container.is-reject-all-enabled div.con-wizard form.consent-form div.wizard-body div.actions.couple button.btn.secondary.accept-all.consent_reject_all_3"))).click()
numeri=[1,4]
lista_tot=[]
azioni=['AAME','AAPL','ACB','ABNB','ACLS','ADES','APD','AMZN','META','TSLA','F','MSFT','CNHI','CNXN','EAR','EBAY','ECC','NKE','ELSE','FOSL','FTI','GDOT','GES','GILT','GM','GTIM','HTOO','AMP'] 
time.sleep(3)
for azione in azioni:
	driver.get(f'https://it.finance.yahoo.com/quote/{azione}/profile?p={azione}')
	dizio={}
	for num in numeri:
		a=driver.find_element(By.CSS_SELECTOR, f"div > p.D\(ib\).Va\(t\) > span:nth-child({num})").text 
		a=a.replace("Settore/i","Categoria")
		b=driver.find_element(By.CSS_SELECTOR, f"div > p.D\(ib\).Va\(t\) > span:nth-child({num+1})").text
		c={a:b}
		d=({'Stock':f'{azione}'})
		d.update(c)
		dizio.update(d)
	print(dizio)

	df = pd.DataFrame(dizio,index=[f'{azione}'])
	df=df.reset_index(drop=True)
	df=df.set_index('Stock')
	print(df)
	lista_tot.append(df)
result=pd.concat(lista_tot)
print(result)
result.to_csv('ziooo.csv')



# print(element.text))
# print(element.text)}
# element =driver.find_element(By.CSS_SELECTOR, "div > p.D\(ib\).Va\(t\) > span:nth-child(1)")
# print(element.text)
driver.quit()


#p.D\(ib\):nth-child(2)
#Col1-0-Profile-Proxy > section > div.asset-profile-container > div > div > p.D\(ib\).Va\(t\) > span:nth-child(2)