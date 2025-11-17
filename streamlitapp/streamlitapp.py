import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_resource
def mySql():
	conn = st.connection('mysql', type='sql')
	df = conn.query('SELECT temp FROM temperature;',ttl=600)
	return df

def main():
	st.title("Plot data from MySql")
	st.write("Temperature")
	data = mySql()

	df2 = pd.DataFrame(data, columns=["temp"])
	temp = px.line(df2, x=df2.index, y="Temp")
	st.plotly_chart(temp, use_container_width=True)

if __name__ == "__main__":
	main()
