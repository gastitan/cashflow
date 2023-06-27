import datetime
from scipy import optimize 

def xnpv(rate,cashflows):
    chron_order = sorted(cashflows, key = lambda x: x[0])
    t0 = chron_order[0][0] #t0 is the date of the first cash flow

    return sum([cf/(1+rate)**((t-t0).days/365.0) for (t,cf) in chron_order])
    

def xirr(cashflows,guess=0.1):

    return optimize.newton(lambda r: xnpv(r,cashflows),guess)*100


def tir(cashflow, precio, plazo):
    flujo_total=[(datetime.datetime.today()+ datetime.timedelta(days=plazo) , -precio)]
    for i in range (len(cashflow)):
      if cashflow.iloc[i,0].to_pydatetime()>datetime.datetime.today()+ datetime.timedelta(days=plazo):
        flujo_total.append((cashflow.iloc[i,0].to_pydatetime(),cashflow.iloc[i,1]))
    
    return round(xirr(flujo_total,guess=0.1),2)
    
