import streamlit as st
import pandas as pd
import numpy as np
    
st.title('Open Pub')
st.markdown('Assuming I’am on a vacation in the United Kingdom with friends. Just for some fun, we decided to go to the Pubs nearby for some drinks. Google Map is down because of some issues. While searching the internet, we came across https://www.getthedata.com/open-pubs. On this website, we found all the pub locations (Specifically Latitude and Longitude info). In order to impress my friends, i decided to create a web application with the data available.')

st.header('Open Pub Data')
df = pd.read_csv('data/clean_open_pubs_data.csv')
st.dataframe(df)

st.header('Shape of Data')
st.dataframe(df.shape)
st.text('There is 50,563 active pubs in United Kingdom')
st.subheader('The total number of rows in the data are :') 
