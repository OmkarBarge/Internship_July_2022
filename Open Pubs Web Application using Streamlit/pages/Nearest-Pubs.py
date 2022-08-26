

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Nearest Pub"
)

df = pd.read_csv('data/clean_open_pubs_data.csv')
st.title('Nearest Pubs base on Latitude and Longitude.')




lat = st.number_input('The latitude of place')
lon = st.number_input('The longitude of place')
button = st.button("Submit Local Authority")
df_new = df[['latitude', 'longitude']]
new_points = np.array([lat, lon])

# Calculate distance between new_points and all points in df_new using Euclidean distance 
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))


# sort the array using arg partition and keep only 5 elements
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.text("The location corresponding to below minimum distances : ")
    st.dataframe(df.iloc[min_indices])
    st.text("The minimum distances are:")
    st.dataframe(distances.head(5))
    st.map(df.iloc[min_indices])