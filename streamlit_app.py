import streamlit as st 
import pandas as pd
import http.client
import json
from io import StringIO

st.set_page_config(
    page_title="VETlab - Interpretacja wyników badań",
    page_icon=":microscope:",  # add a lab microscope icon as the app icon
    layout="wide"
)

# st.balloons()
st.image("https://vetnolimits.com/wp-content/uploads/2020/11/vetnolimits_logo__color-m.png")
st.markdown("# VETnolimitsLAB")
st.markdown("## Interpretacja wyników badań")

st.divider()

st.markdown("### 🩸 KREW")

st.write("Wybierz parametr i jego stan:")

conn = http.client.HTTPSConnection("app.nocodb.com")
headers = { 'xc-token': "0At1GzBrfpYclyW568ViqVKwYbaOf10vcFo8hnu7" }
conn.request("GET", "/api/v2/tables/mf02p7riniazneb/records?offset=0&limit=25&where=&viewId=vwpruy8w3xndb3v6", headers=headers)
response = conn.getresponse()
res = response.read()
jsondata = res.decode("utf-8")
# s = str(response,"utf-8")
# data = StringIO(s)
# df = pd.read_csv(data)
# st.write(decoded)

parsed_data = json.loads(jsondata)

df = pd.DataFrame(
    data=parsed_data['list'],
    columns=['Parametr', 'Obniżony parametr ⬇︎', 'Podwyższony parametr ⬆︎']
    )

# dfdown = pd.DataFrame(
#     data=parsed_data['list'],
#     columns=['Obniżony parametr ⬇︎']
#     )
# dfup = pd.DataFrame(
#     data=parsed_data['list'],
#     columns=['Podwyższony parametr ⬆︎']
#     )
# dfp = pd.DataFrame(
#     data=parsed_data['list'],
#     columns=["Parametr"]
#     )

parametr = df['Parametr'].drop_duplicates()
down = df['Obniżony parametr ⬇︎'].drop_duplicates()
up = df['Podwyższony parametr ⬆︎'].drop_duplicates()

wybor = st.selectbox(
    "Parametr",
    parametr
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Obniżony parametr ⬇︎")
    down_value = df.loc[df['Parametr'] == wybor, 'Obniżony parametr ⬇︎'].values[0]
    st.write(down_value)

with col2:
    st.markdown("#### Podwyższony parametr ⬆︎")
    up_value = df.loc[df['Parametr'] == wybor, 'Podwyższony parametr ⬆︎'].values[0]
    st.write(up_value)

# st.dataframe(
#     data=df,
#     hide_index=True,
#     )





