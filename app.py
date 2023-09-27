import streamlit as st
import pandas as pd
from mitosheet.streamlit.v1 import spreadsheet

st.set_page_config(layout="wide")
st.title("Data Cleaning Verification")

st.markdown("""
    In order to use the in-house data science solution, you must ensure that the data types are correct. 

    1. Upload your data
    2. Verify that the data types of each column are correct
    3. Export the cleaned data as a Pickle file
""")


# Display the data inside of the spreadsheet so the user can easily fix data quality issues.
dfs, _ = spreadsheet(import_folder='./data')

no_dataframes = len(dfs) == 0

df = list(dfs.values())[0] if not no_dataframes else None
df_name = list(dfs.keys())[0] if not no_dataframes else None

message = ''
if no_dataframes: 
    message = "You must upload a file before exporting the cleaned data."
else: 
    message = "Your file has less than 1 million rows, so you can export it as an XLSX file."
st.markdown(message)

pickle_button = st.button("Download as Pickle file", key='pickle_button', disabled=no_dataframes)

if pickle_button:
    df.to_pickle(f"{df_name}.pkl")
    st.success(f'Downloaded {df_name} as Pickle file.')

