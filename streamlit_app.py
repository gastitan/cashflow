import streamlit as st
import tir as t
import import_cashflow as cf
import pandas as pd

st.title("El site de tu vida")

all_cashflows = {}
lista = []

def tir_alert():
	for i in cf.Data_ON.index:
		try:
			CF=pd.read_excel('cashflows_ON.xlsx', sheet_name=i)
			all_cashflows[i]=CF
		except:
			pass

	for ticker in cf.Data_ON.index:
		try:
			cashflow = all_cashflows[ticker]
			precio = cf.Data_ON.loc[ticker,'Precio_dolares']
			
			tir = t.tir(cashflow, precio, plazo=2)

			if tir > 9:
				#print("ALERTA %s - Price: %s - TIR: %s" % (ticker, precio, tir))
				lista.append([ticker, precio, tir])
		except:
			pass

tir_alert()
df = pd.DataFrame(lista, columns = ('Ticker', 'Price', 'TIR'))
st.table(df)
