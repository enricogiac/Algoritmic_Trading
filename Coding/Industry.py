azioni=['AAME','AAPL','ACB','ABNB','ACLS','ADES','APD','AMZN','META','TSLA','F','MSFT','CNHI','CNXN','EAR','EBAY','ECC','NKE','ELSE','FOSL','FTI','GDOT','GES','GILT','GM','GTIM','HTOO','ADS','AMP'] 
numeri=[1,2,3,4,5,6,7,8,9,10]
for azione in azioni:
	#print(f"{azione}")

	dizio_tot=[]
	
	for num in numeri:
		print(f"{azione} e pag {num}")


		driver.get(f"https://www.barchart.com/stocks/quotes/{azione}/income-statement/annual?reportPage={num}")
		try:
			WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"html body.hide-menu-for-landscape.add-ads-premier div.a__sc-np32r2-0.eqYWHN div.Card-sc-1s2p2gv-0.a__sc-3vtlsk-0.kDNyTh.jXixFa div.Card__CardHeader-sc-1s2p2gv-1.a__sc-3vtlsk-1.fZGtpv.cVIXeq div.Frame-sc-1d4hofp-0.fRUcSy button.Button__StyledButton-a1qza5-0.jkvvVr"))).click()
		except:
			pass
		