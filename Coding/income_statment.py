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
fataframes=[]
azioni=['AAME','AAPL','ACB','ABNB','ACLS','ADES','APD','AMZN'] 
numeri=[1,2,3]
for azione in azioni:
    print(f"{azione}")

    dizio_tot=[]
    
    for num in numeri:
        print(f"{azione} e pag {num}")

        driver.get(f"https://www.barchart.com/stocks/quotes/AAPL/income-statement/quaterly?reportPage=1")
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html body.hide-menu-for-landscape.add-ads-premier div.a__sc-np32r2-0.eqYWHN div.Card-sc-1s2p2gv-0.a__sc-3vtlsk-0.kDNyTh.jXixFa div.Card__CardHeader-sc-1s2p2gv-1.a__sc-3vtlsk-1.fZGtpv.cVIXeq div.Frame-sc-1d4hofp-0.fRUcSy button.Button__StyledButton-a1qza5-0.jkvvVr"))).click()
        except:
            pass

                #time.sleep(3)


        values=driver.find_elements(By.CSS_SELECTOR, "html body.hide-menu-for-landscape.add-ads-premier main#bc-main-content-wrapper.off-canvas-wrap.ng-isolate-scope div.inner-wrap div.main-content-wrapper.content.js-main-content-wrapper div.row div.large-12.columns div.one-column-block div.row div#main-content-column.small-12.columns.main-column div.column-inner div.bc-financial-report div.bc-table-scrollable div.bc-table-scrollable-inner ng-transclude table.ng-scope tbody tr td")

        print(len(values))
        lista=[]
        for value in values:
            print(value.text)
            lista.append(value.text)
        print(lista)
        if len(lista)==0:
            continue

        for val in lista:
            if val==' ':
                lista.remove(val)
            else:
                pass
                     
        print(lista)
        print(len(lista))

        lista2=[]
        if (len(lista)-5)%6==0:
            i=0
            k=4
            while i<=k:
                lista2.append(lista[i])
                i+=1
            print(lista2)
            for value in lista2:
                lista.remove(value)
            print(len(lista))
            print("")
            print(lista)
            print("")
            dic={}
            i=0
            if len(lista2)==5:
                while i<=len(lista):
                    dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3],lista[i+4],lista[i+5]]})
                    i+=6
                    if i==len(lista):
                        break
                print(dic)
        elif (len(lista)-4)%5==0:
            i=0
            k=3
            while i<=k:
                lista2.append(lista[i])
                i+=1
            print(lista2)
            for value in lista2:
                lista.remove(value)
            print(len(lista))
            print("")
            print(lista)
            print("")
            dic={}
            i=0
            if len(lista2)==4:
                while i<=len(lista):
                    dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3],lista[i+4]]})
                    i+=5
                    if i==len(lista):
                        break
                print(dic)

        elif (len(lista)-3)%4==0:
            i=0
            k=2
            while i<=k:
                lista2.append(lista[i])
                i+=1
            print(lista2)
            for value in lista2:
                lista.remove(value)
            print(len(lista))
            print("")
            print(lista)
            print("")
            dic={}
            i=0
            if len(lista2)==3:
                while i<=len(lista):
                    dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3]]})
                    i+=4
                    if i==len(lista):
                        break
                print(dic)
        elif (len(lista)-2)%3==0:
            i=0
            k=1
            while i<=k:
                lista2.append(lista[i])
                i+=1
            print(lista2)
            for value in lista2:
                lista.remove(value)
            print(len(lista))
            print("")
            print(lista)
            print("")
            dic={}
            i=0
            if len(lista2)==2:
                while i<=len(lista):
                    dic.update({lista[i]:[lista[i+1],lista[i+2]]})
                    i+=3
                    if i==len(lista):
                        break
                print(dic)

                    

        dic1={"year":lista2}
        dic1.update(dic)
        df = pd.DataFrame(dic1,index=lista2)
        df=df.assign(Azione=f"{azione}")
                #df.drop(df.columns[[0]], axis = 1)
        dizio_tot.append(df)

    if len(dizio_tot)>0:
        result=pd.concat(dizio_tot)
        print(result)
    else:
            continue
    fataframes.append(result)
    #result.to_csv(f"dati{azione}.csv")
driver.quit()   
fataframes_1=pd.concat(fataframes)
print(fataframes_1)
fataframes_1=fataframes_1.reset_index(drop=True)
print(fataframes_1)
# fataframes_1.to_csv("boh.csv")

