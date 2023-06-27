import tir as t
import requests
import app_notifications as notifier
import import_cashflow as cf
import pandas as pd

#tickers = ['CP21O']

all_cashflows = {}
for i in cf.Data_ON.index:
	try:
		CF=pd.read_excel('cashflows_ON.xlsx', sheet_name=i)
		all_cashflows[i]=CF
	except:
		pass

for ticker in cf.Data_ON.index:
#for ticker in tickers:
	try:
		#print(ticker)
		cashflow = all_cashflows[ticker]
		precio = cf.Data_ON.loc[ticker,'Precio_dolares']
		
		tir = t.tir(cashflow, precio, plazo=2)
		#print("ticker %s %s" % (ticker, tir))

		if tir > 9:
			print("ALERTA %s - Price: %s - TIR: %s" % (ticker, precio, tir))
			#titulo = "Alerta TIR"
			#mensaje = "La TIR de %s es %s" % (ticker, tir)
			#notifier.enviar_notificacion(titulo, mensaje)
	except:
		pass
