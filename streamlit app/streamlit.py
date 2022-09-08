
import pandas as pd
import streamlit as st
from railway_db import *
from config import config
import plotly.express as px
import psycopg2

header_container = st.container()
stats_container = st.container()	
with header_container:


	st.header("Data Base Visualization")
	st.subheader("Welcome!")

with stats_container:

	conn = connect()
	query = st.text_input('Query' )
	data=run_query(conn, query)
	
	df = pd.DataFrame (data, columns = ['Houses', 'Address', 'Rooms','Dates','Rent'])
	df.drop_duplicates(inplace=True)
	df.index.is_unique
	st.write(df)






