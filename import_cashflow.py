import numpy as np
import pandas as pd

url = "https://iol.invertironline.com/mercado/cotizaciones/argentina/obligaciones%20negociables"
ON = pd.read_html(url)[0]

precios_ON=pd.DataFrame()
precios_ON['Último Operado']=ON['Último Operado'].str.replace('.','').str.replace(',','.').astype(float)
try:
  precios_ON['MontoOperado']=ON['MontoOperado'].str.replace('.','').str.replace(',','.').astype(float)
except:
  precios_ON['MontoOperado']=0
  
precios_ON['Ticker']=ON['Símbolo']
precios_ON=precios_ON[['Ticker','Último Operado','MontoOperado']]
precios_ON.set_index('Ticker',inplace=True)

Data_ON=tickers=pd.read_excel('cashflows_ON.xlsx', sheet_name='Data_ON')
comunes=list(set(precios_ON.index) & set(Data_ON['ticker_dolares']))
comunes.sort()
Data_ON=Data_ON.loc[Data_ON['ticker_dolares'].isin(comunes)].sort_values(by=['ticker_dolares'])
Data_ON['Precio_dolares']=list(precios_ON.loc[comunes]['Último Operado']/100)
Data_ON['Volumen']=list(precios_ON.loc[comunes]['MontoOperado'])

Data_ON['Precio_pesos']=0

try:
  Data_ON['Precio_pesos']=list(precios_ON.loc[Data_ON['ticker_pesos']]['ÚltimoOperado'])
  Data_ON['Volumen']=list(precios_ON.loc[Data_ON['ticker_pesos']]['MontoOperado'])
except:
  for ticker in Data_ON['ticker_pesos']:
    if ticker in precios_ON.index:
      Data_ON.loc[Data_ON['ticker_pesos']==ticker,'Precio_pesos']=precios_ON.loc[ticker]['Último Operado']

Data_ON['Amortizacion']=Data_ON['Amortizacion'].replace(np.nan, 'No Bullet', regex=True)
Data_ON.set_index(['ticker_pesos'], inplace=True)
Data_ON
