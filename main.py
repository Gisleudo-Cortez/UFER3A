from module import *
import investpy
import mplfinance as mpf
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data_inicial = '21/08/2016'
data_final = '21/08/2021'

pais = 'brazil'
etf = ETF('bova11', pais)
acao = Acao('VALE3', pais)
	
print(acao.beta(etf,data_inicial, data_final, plot = False))