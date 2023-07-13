import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
         ## A Simple Stock Price App

         Shown are the stock closing price and volume of Top Glove

         Inpired by ****Soon Meei Weon****       
""")

tickerSymbol = '7113.KL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d',start='2010-5-31',end='2023-5-31')

st.write(""" 
****Closing Price****
""")
st.line_chart(tickerDF.Close)

st.write(""" 
****Volume****
""")
st.line_chart(tickerDF.Volume)

