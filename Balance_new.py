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
from tqdm import tqdm
import re


driver=webdriver.Firefox()
fataframes=[]
a1=["AFTR", "AFYA", "AG", "AGAC", "AGAE", "AGBA", "AGBAW", "AGCO", "AGD",
    "AGE", "AGEN", "AGFY", "AGI", "AGIL", "AGILW", "AGIO", "AGL", "AGLE",
    "AGM", "AGM^C", "AGM^D", "AGM^E", "AGM^F", "AGM^G", "AGMH", "AGNC",
    "AGNCL", "AGNCM", "AGNCN", "AGNCO", "AGNCP", "AGO", "AGR", "AGRI",
    "AGRIW", "AGRO", "AGRX", "AGS", "AGTI", "AGX", "AGYS", "AHCO", "AHG",
    "AHH", "AHH^A", "AHI", "AHL^C", "AHL^D", "AHL^E", "AHRN", "AHRNU",
    "AHT", "AHT^D", "AHT^F", "AHT^G", "AHT^H", "AHT^I", "AI", "AIB", "AIC",
    "AIF", "AIG", "AIG^A", "AIH", "AIHS", "AIM", "AIMAU", "AIMD", "AIMDW",
    "AIN", "AINC", "AIO", "AIP", "AIR", "AIRC", "AIRG", "AIRI", "AIRS",
    "AIRT", "AIRTP", "AIT", "AIU", "AIV", "AIXI", "AIZ", "AIZN", "AJG",
    "AJRD", "AJX", "AJXA", "AKA", "AKAM", "AKAN", "AKBA", "AKLI", "AKO/A",
    "AKO/B", "AKR", "AKRO", "AKTS", "AKTX", "AKU", "AKYA", "AL", "AL^A",
    "ALAR", "ALB", "ALBT", "ALC", "ALCC", "ALCO", "ALCYU", "ALDX", "ALE",
    "ALEC", "ALEX", "ALG", "ALGM", "ALGN", "ALGS", "ALGT", "ALHC", "ALIM",
    "ALIT", "ALK", "ALKS", "ALKT", "ALL", "ALL^B", "ALL^H", "ALL^I", "ALLE",
    "ALLG", "ALLK", "ALLO", "ALLR", "ALLT", "ALLY", "ALNY", "ALOR", "ALORU",]
a2=[ "ALOT", "ALPA", "ALPAU", "ALPAW", "ALPN", "ALPP", "ALPS", "ALRM", "ALRN",
    "ALRS", "ALSA", "ALSAR", "ALSAW", "ALSN", "ALT", "ALTG", "ALTG^A", "ALTI",
    "ALTIW", "ALTO", "ALTR", "ALTU", "ALTUW", "ALV", "ALVO", "ALVR", "ALX",
    "ALXO", "ALYA", "ALZN", "AM", "AMAL", "AMAM", "AMAO", "AMAOU", "AMAT",
    "AMBA", "AMBC", "AMBI", "AMBO", "AMBP", "AMC", "AMCR", "AMCX", "AMD",
    "AME", "AMED", "AMEH", "AMG", "AMGN", "AMH", "AMH^G", "AMH^H", "AMK",
    "AMKR", "AMLI", "AMLX", "AMN", "AMNB", "AMOT", "AMP", "AMPE", "AMPG",
    "AMPGW", "AMPH", "AMPL", "AMPS", "AMPX", "AMPY", "AMR", "AMRC", "AMRK",
    "AMRN", "AMRS", "AMRX", "AMS", "AMSC", "AMSF", "AMST", "AMSWA", "AMT",
    "AMTB", "AMTD", "AMTI", "AMTX", "AMV", "AMWD", "AMWL", "AMX", "AMZN",
    "AN", "ANAB", "ANDE", "ANEB", "ANET", "ANF", "ANGH", "ANGHW", "ANGI",
    "ANGN", "ANGO", "ANIK", "ANIP", "ANIX", "ANNX", "ANPC", "ANSS", "ANTE",
    "ANTX", "ANVS", "ANY", "ANZU", "ANZUU", "ANZUW", "AOD", "AOGO", "AOGOU",
    "AOMR", "AON", "AORT", "AOS", "AOSL", "AOUT", "AP", "APA", "APAC",
    "APACW", "APAM", "APCA", "APCX", "APCXW", "APD", "APDN", "APE", "APEI"]
a3=["APG", "APGB", "APGN", "APGNW", "APH", "API", "APLD", "APLE", "APLM",
    "APLMW", "APLS", "APLT", "APM", "APMI", "APMIU", "APMIW", "APO", "APOG",
    "APP", "APPF", "APPH", "APPHW", "APPN", "APPS", "APRE", "APRN", "APT",
    "APTM", "APTMU", "APTMW", "APTO", "APTV", "APTV^A", "APTX", "APVO",
    "APWC", "APXI", "APXIU", "APXIW", "APYX", "AQB", "AQMS", "AQN", "AQNA",
    "AQNB", "AQNU", "AQST", "AQU", "AQUA", "AQUNR", "AR", "ARAV", "ARAY",
    "ARBB", "ARBE", "ARBEW", "ARBG", "ARBGW", "ARBK", "ARBKL", "ARC", "ARCB",
    "ARCC", "ARCE", "ARCH", "ARCO", "ARCT", "ARDC", "ARDS", "ARDX", "ARE",
    "AREB", "AREBW", "AREC", "AREN", "ARES", "ARGD", "ARGO", "ARGO^A", "ARGX",
    "ARHS", "ARI", "ARIS", "ARIZ", "ARIZR", "ARIZU", "ARIZW", "ARKO", "ARKOW",
    "ARKR", "ARL", "ARLO", "ARLP", "ARMK", "ARMP", "ARNC", "AROC", "AROW",
    "ARQQ", "ARQQW", "ARQT", "ARR", "ARR^C", "ARRW", "ARRWU", "ARRWW", "ARRY",
    "ARTE", "ARTEU", "ARTL", "ARTLW", "ARTNA", "ARTW", "ARVL", "ARVN", "ARW",
    "ARWR", "ARYD", "ARYE", "ASA", "ASAI", "ASAN", "ASB", "ASB^E", "ASB^F",
    "ASBA", "ASC", "ASCA", "ASCAU", "ASCB", "ASCBU", "ASCBW", "ASG", "ASGI",
    "ASGN", "ASH", "ASIX", "ASLE", "ASLN", "ASM", "ASMB", "ASML", "ASND",
    "ASNS", "ASO", "ASPI", "ASPN", "ASPS", "ASR", "ASRT", "ASRV", "ASST",
    "ASTC", "ASTE", "ASTI", "ASTL", "ASTLW", "ASTR", "ASTS", "ASTSW", "ASUR",
    "ASX", "ASXC", "ASYS", "ATAI", "ATAK", "ATAKW", "ATAQ", "ATAT", "ATCO^D",
    "ATCO^H", "ATCO^I", "ATCOL", "ATEC", "ATEK", "ATEN", "ATER", "ATEX",
    "ATGE", "ATH^A", "ATH^B", "ATH^C", "ATH^D", "ATH^E", "ATHA", "ATHE",
    "ATHM", "ATHX", "ATI", "ATIF", "ATIP", "ATKR", "ATLC", "ATLCL", "ATLCP",
    "ATLO", "ATLX", "ATMC", "ATMCU", "ATMCW", "ATMVU", "ATNF", "ATNFW", "ATNI",
    "ATNM", "ATNX", "ATO", "ATOM", "ATOS", "ATR", "ATRA", "ATRC", "ATRI",
    "ATRO", "ATSG", "ATTO", "ATUS", "ATVI", "ATXG", "ATXI", "ATXS", "AU",
    "AUB", "AUB^A", "AUBN"]

azioni=[a1,a2,a3]

numeri=[1,2,3,4,5,6,7,8,9,10]
regex = r'\d{2}-\d{4}'
driver.implicitly_wait(10)
for azione in tqdm(azioni):
	for a in azione:
	    print(f"{azione}")
	dizio_tot=[]   
	    for num in numeri:
	        print(f"{azione} e pag {num}")
	       # driver.get(f"https://www.barchart.com/stocks/quotes/{azione}/balance-sheet/quarterly?reportPage={num}")
	        try:
	            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html body.hide-menu-for-landscape.add-ads-premier.modal-open div.reveal-modal.fade.bc-nui-auth-modal.bc-nui-auth-blue-modal.register-modal.authentication-modal.auth-no-modal-ref-class.in div div.bc-modal-login.bc-nui-modal-login.ng-scope div.form-close-wrapper.ng-scope i.bc-glyph-times.form-close"))).click()
	        except:
	        	pass
	        try:
	            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html body.hide-menu-for-landscape.add-ads-premier div.a__sc-np32r2-0.eqYWHN div.Card-sc-1s2p2gv-0.a__sc-3vtlsk-0.kDNyTh.jXixFa div.Card__CardHeader-sc-1s2p2gv-1.a__sc-3vtlsk-1.fZGtpv.cVIXeq div.Frame-sc-1d4hofp-0.fRUcSy button.Button__StyledButton-a1qza5-0.jkvvVr"))).click()
	        except:
	        	pass
	       # time.sleep(3)
	        button=driver.find_element(By.CSS_SELECTOR, "html body.hide-menu-for-landscape.add-ads-premier main#bc-main-content-wrapper.off-canvas-wrap.ng-isolate-scope div.inner-wrap div.main-content-wrapper.content.js-main-content-wrapper div.row div.large-12.columns div.one-column-block div.row div#main-content-column.small-12.columns.main-column div.column-inner div.bc-financial-report div.bc-financial-report__pagination.clearfix div.right a.bc-button.light-blue.ok").text
	        print(button)
	        if (num==1):

	        	pass
	        elif (button!="NEXT"):
	        	break
	        else:

	        	try:

	        		WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html body.hide-menu-for-landscape.add-ads-premier main#bc-main-content-wrapper.off-canvas-wrap.ng-isolate-scope div.inner-wrap div.main-content-wrapper.content.js-main-content-wrapper div.row div.large-12.columns div.one-column-block div.row div#main-content-column.small-12.columns.main-column div.column-inner div.bc-financial-report div.bc-financial-report__pagination.clearfix div.right a.bc-button.light-blue.ok"))).click()
	        	except:
	        		continue


	                #time.sleep(3)


	        values=driver.find_elements(By.CSS_SELECTOR, "html body.hide-menu-for-landscape.add-ads-premier main#bc-main-content-wrapper.off-canvas-wrap.ng-isolate-scope div.inner-wrap div.main-content-wrapper.content.js-main-content-wrapper div.row div.large-12.columns div.one-column-block div.row div#main-content-column.small-12.columns.main-column div.column-inner div.bc-financial-report div.bc-table-scrollable div.bc-table-scrollable-inner ng-transclude table.ng-scope tbody tr td")

	        print(len(values))
	        lista=[]
	        for value in values:
	            #print(value.text)
	            lista.append(value.text)
	       # print(lista)
	        if len(lista)==0:
	            break
	        new = []
	        for val in lista:
	            if val.strip() != '' and val != 'Current Assets' and val != "Non-Current Assets" and val != "Current Liabilities" and val != "Non-Current Liabilities" and val!='ASSETS' and val!='LIABILITIES'and val!="SHAREHOLDERS' EQUITY":
	                new.append(val)

	        #print(new)
	        #print(len(new))
	        lista=new
	        lista2=[]
	        for val in lista:
	            corrispondenze = re.findall(regex, val)
	            if corrispondenze:
	                lista2.extend(corrispondenze)
	        #print(lista2)
	        for val in lista2:
	            lista.remove(val)
	        #print(lista)
	        dic={}
	        i=0
	        if len(lista2)==5:
	            while i<=len(lista):
	                dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3],lista[i+4],lista[i+5]]})
	                #print(dic)
	                i+=6
	                if i==len(lista):
	                    break
	        elif len(lista2)==4:
	            while i<=len(lista):
	                dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3],lista[i+4]]})
	                i+=5
	                if i==len(lista):
	                    break
	        elif len(lista2)==3:
	            while i<=len(lista):
	                dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3]]})
	                i+=4
	                if i==len(lista):
	                    break
	        elif len(lista2)==2:
	            while i<=len(lista):
	                dic.update({lista[i]:[lista[i+1],lista[i+2]]})
	                i+=3
	                if i==len(lista):
	                    break
	        else:
	            while i<=len(lista):
	                dic.update({lista[i]:[lista[i+1]]})
	                i+=2
	                if i==len(lista):
	                    break


	        #print(dic)
	        # if len(new)<100:
	        #     continue
	        # lista=new
	        # lista2=[]
	        # if (len(lista)-5)%6==0 and (len(lista)-5)/6>14:
	        #     i=0
	        #     k=4
	        #     while i<=k:
	        #         lista2.append(lista[i])
	        #         i+=1
	        #     print(lista2)
	        #     for value in lista2:
	        #         lista.remove(value)
	        #     print(len(lista))
	        #     print("")
	        #     print(lista)
	        #     print("")
	        #     dic={}
	        #     i=0
	        #     if len(lista2)==5:
	        #         while i<=len(lista):
	        #             dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3],lista[i+4],lista[i+5]]})
	        #             print(dic)
	        #             i+=6
	        #             if i==len(lista):
	        #                 break
	        #         print(dic)
	        # elif (len(lista)-4)%5==0:
	        #     i=0
	        #     k=3
	        #     while i<=k:
	        #         lista2.append(lista[i])
	        #         i+=1
	        #     print(lista2)
	        #     for value in lista2:
	        #         lista.remove(value)
	        #     print(len(lista))
	        #     print("")
	        #     print(lista)
	        #     print("")
	        #     dic={}
	        #     i=0
	        #     if len(lista2)==4:
	        #         while i<=len(lista):
	        #             dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3],lista[i+4]]})
	        #             i+=5
	        #             if i==len(lista):
	        #                 break
	        #         print(dic)

	        # elif (len(lista)-3)%4==0:
	        #     i=0
	        #     k=2
	        #     while i<=k:
	        #         lista2.append(lista[i])
	        #         i+=1
	        #     print(lista2)
	        #     for value in lista2:
	        #         lista.remove(value)
	        #     print(len(lista))
	        #     print("")
	        #     print(lista)
	        #     print("")
	        #     dic={}
	        #     i=0
	        #     if len(lista2)==3:
	        #         while i<=len(lista):
	        #             dic.update({lista[i]:[lista[i+1],lista[i+2],lista[i+3]]})
	        #             i+=4
	        #             if i==len(lista):
	        #                 break
	        #         print(dic)
	        # elif (len(lista)-2)%3==0:
	        #     i=0
	        #     k=1
	        #     while i<=k:
	        #         lista2.append(lista[i])
	        #         i+=1
	        #     print(lista2)
	        #     for value in lista2:
	        #         lista.remove(value)
	        #     print(len(lista))
	        #     print("")
	        #     print(lista)
	        #     print("")
	        #     dic={}
	        #     i=0
	        #     if len(lista2)==2:
	        #         while i<=len(lista):
	        #             dic.update({lista[i]:[lista[i+1],lista[i+2]]})
	        #             i+=3
	        #             if i==len(lista):
	        #                 break
	        #         print(dic)

	                    

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
	fataframes_1.to_csv(f"Balance_dati{azione}.csv")

# #acb pag lista2