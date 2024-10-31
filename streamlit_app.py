import streamlit as st
import pandas as pd
import http.client
from config import API_KEY, HOST, TABLE_ID, VIEW_ID
import json

st.set_page_config (page_title="Vetnolimits Lab")

st.header("Vetnolimits Lab")
st.subheader("Twoja pomoc w diagnostyce różnicowej")

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

conn.close()