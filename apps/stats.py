import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json


def convert_df(df):
    return df.to_csv().encode('utf-8')

def app():

    st.title("General Stats for NFTs (does not track sales)")
    st.text('sales stats can be found at the links below')
    st.write("Knowhere - [https://share.streamlit.io/kmonee/knowhere-sales-dash/main/kw_app.py](https://share.streamlit.io/kmonee/knowhere-sales-dash/main/kw_app.py)")
    st.write("RandomEarth - [https://share.streamlit.io/kmonee/randomearth-sales-dash/main/sales_app.py](https://share.streamlit.io/kmonee/randomearth-sales-dash/main/sales_app.py)")
    st.markdown("""---""")

    active_address = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8bda381f-354a-489d-917b-f5d47e2e7113/data/latest')

    col1, col2 = st.columns([1,3])

    col1.header("Active addresses - Past 30 days")
    col1.text("""Defined as addresses which interacted 
with a contract or minted an NFT \n
Does not count addresses that only hold""")
    col1.dataframe(active_address)

    active_csv = convert_df(pd.DataFrame(active_address))


    col1.download_button(
    "Press to Download",
    active_csv,
    "active_addresses.csv",
    "text/csv",
    key='download-csv'
    )

    col2.header("**Graph to be inserted below**")
    col2.metric("Count of active addresses during the past 30 days", len(active_address))

    st.text('')
    st.header("Unique addresses holding Levana NFTs")
    total_nft_holders = pd.read_csv('http://165.22.125.123/address_count_stats.csv')

    holder_graph = px.line(
        total_nft_holders,
        x = "TIMESTAMP",
        color = "NFT",
        y = "UNIQUE_ADDRESS_COUNT",
        width = 1350
    )

    #st.dataframe(total_nft_holders)
    st.plotly_chart(holder_graph)






    # df = pd.DataFrame(rarity_counts)
    # fig = px.pie(df, values='traits', names=df.index)
    # col2.plotly_chart(fig, use_column_width=True)