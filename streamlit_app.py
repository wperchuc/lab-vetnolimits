import streamlit as st
import pandas as pd
import http.client
from config import API_KEY, HOST, TABLE_ID, VIEW_ID
import json

### START OF DEBUG

from dotenv import load_dotenv
import os

st.set_page_config (page_title="🔬 Vetnolimits Lab")

# Load environment variables
load_dotenv()

# # Debug: Print all environment variables
# st.write("Checking environment variables:")
# HOST = st.secrets('NOCODB_HOST')
# API_KEY = st.secrets('NOCODB_API_KEY')
# TABLE_ID = st.secrets('NOCODB_TABLE_ID')
# VIEW_ID = st.secrets('NOCODB_VIEW_ID')

# st.write({
#     'HOST': HOST,
#     'API_KEY': '***' if API_KEY else None,
#     'TABLE_ID': TABLE_ID,
#     'VIEW_ID': VIEW_ID
# })

# Only proceed if HOST is available
if HOST:
    conn = http.client.HTTPSConnection(HOST)
    headers = {'xc-token': API_KEY}
    endpoint = f"/api/v2/tables/{TABLE_ID}/records?offset=0&limit=25&where=&viewId={VIEW_ID}"
    conn.request("GET", endpoint, headers=headers)
else:
    st.error("HOST environment variable is not set!")

### END OF DEBUG

st.header("Vetnolimits Lab")
st.subheader("Twoja pomoc w diagnostyce różnicowej")

# Add custom CSS for better styling
st.markdown("""
    <style>
    .stSelectbox {
        margin-bottom: 2rem;
    }
    .diagnostic-card {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .lowered {
        background-color: #EFF6FF;
    }
    .elevated {
        background-color: #FEF2F2;
    }
    </style>
""", unsafe_allow_html=True)

st.write("Wybierz parametr i jego stan, aby zobaczyć sugerowane diagnozy.")

conn = http.client.HTTPSConnection(HOST)

headers = { 'xc-token': API_KEY }

conn.request("GET", f"/api/v2/tables/{TABLE_ID}/records?offset=0&limit=25&where=&viewId={VIEW_ID}", headers=headers)

res = conn.getresponse()
data = res.read()
json_str = data.decode("utf-8")
data = json.loads(json_str)
df = pd.DataFrame(data['list'])

print(df.columns)

selected_parameter = st.selectbox('Parametr', df.loc[:,'Parametr'].sort_values(), placeholder='Wpisz lub wybierz', index=None)
selected_parameter = str(selected_parameter)

# st.table(df.loc[df['Parametr'] == selected_parameter])

st.dataframe(df.loc[df['Parametr'] == selected_parameter],
             column_order=['Obniżony parametr ⬇︎', 'Podwyższony parametr ⬆︎'],
             use_container_width=True,
             hide_index=True,
             on_select='ignore'
             )

if selected_parameter:
    # Get the data for the selected parameter
    param_data = df.loc[df['Parametr'] == selected_parameter].iloc[0]
    
    # Display the headers first
    st.markdown('### Obniżony parametr ⬇️')
    # Display lowered parameter content in a styled container
    st.markdown(f"""
        <div class="diagnostic-section lowered">
            {param_data['Obniżony parametr ⬇︎']}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('### Podwyższony parametr ⬆️')
    # Display elevated parameter content in a styled container
    st.markdown(f"""
        <div class="diagnostic-section elevated">
            {param_data['Podwyższony parametr ⬆︎']}
        </div>
    """, unsafe_allow_html=True)


conn.close()