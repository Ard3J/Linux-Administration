import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import requests
import os				#os ja dotenv antaa hakea .env tiedostosta salaiset asiat
from dotenv import load_dotenv
from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=600000,limit=None,key="weather_chart")
#refreshaa streamlitin 5min välein, toistaa loputtomiin. Key identifioi, ei varsinaisesti väliä kun toistoja ei lasketa tai rajoiteta


load_dotenv()
USER = os.getenv('MYSQLUSER')
PASSWD = os.getenv('MYSQLPASS')
NEWSAPI = os.getenv('NEWSAPI')

conn = mysql.connector.connect(host='localhost', user=USER, password=PASSWD, database='weather_db')
df = pd.read_sql('SELECT temperature, description, timestamp FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)
conn.close()
st.title('Säädata Oulusta')
chart = px.line(df, x='timestamp',y='temperature')
chart.update_layout(yaxis_title='Lämpötila',xaxis_title='Kellonaika')
st.plotly_chart(chart)
st.dataframe(df)


conn = mysql.connector.connect(host='localhost', user=USER, password=PASSWD, database='jokes')
jd = pd.read_sql('SELECT setup, punchline FROM jokes_data ORDER BY timestamp DESC LIMIT 10',conn)
conn.close()
st.title('"Hauskaa"')
st.dataframe(jd)

