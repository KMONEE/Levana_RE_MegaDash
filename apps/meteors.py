import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json
import ast


def app():

    #st.set_page_config(layout="wide")
    st.title("Meteors")
    st.text ("https://randomearth.io/collections/terra1chrdxaef0y2feynkpq63mve0sqeg09acjnp55v")
    st.text('')

    st.markdown("""
    ---
    """)



    
    meteors = pd.read_csv('http://165.22.125.123/meteor_nfts.csv')
    st.dataframe(meteors)

    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(meteors)

    
    st.download_button(
    "Press to Download",
    csv,
    "meteors.csv",
    "text/csv",
    key='download-csv'
    )

    st.markdown("""
    ---
    """)

    col1, col2 = st.columns([1,3])


    col1.header("Counts of Meteors \n in wallets per rarity")
    rarity_counts = meteors
    #rarity_counts['traits'] = rarity_counts['traits'].apply(lambda x: x.get('Rarity'))
    rarity_counts['traits'] = rarity_counts['traits'].apply(lambda x: ast.literal_eval(x).get('rarity'))
    rarity_counts = rarity_counts['traits'].value_counts()
    #st.dataframe(rarity_counts)
    col1.dataframe(rarity_counts)


    df = pd.DataFrame(rarity_counts)
    fig = px.pie(df, values='traits', names=df.index)
    col2.plotly_chart(fig, use_column_width=True)

    

    st.markdown("""
    ---
    """)

    col3, col4, col5 = st.columns([1,1,1])
    col3.markdown("""## All unique addresses""")

    uniques = meteors['user_addr'].unique()
    col3.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    col3.download_button(
    "Press to Download",
    csv2,
    "unique_address_meteors.csv",
    "text/csv",
    key='download-csv'
    )

    col4.header("""Counts per wallet                 """)


    meteors_per_wallet = meteors['user_addr'].value_counts().reset_index().rename(columns={'user_addr':'meteors_count'})
    col4.dataframe(meteors_per_wallet)

    col4.download_button(
    "Press to Download",
    convert_df(pd.DataFrame(meteors_per_wallet)),
    "meteors_count_per_address.csv",
    "text/csv",
    key='download-csv'
    )

    col5.header("Counts w/ rarity")
    meteors_per_wallet_rarity = meteors[['user_addr', 'traits']].value_counts().reset_index().rename(columns={'user_addr':'meteors_count', 'traits':'rarity', 0:'count'})
    col5.dataframe(meteors_per_wallet_rarity)

    col5.download_button(
    "Press to Download",
    convert_df(pd.DataFrame(meteors_per_wallet_rarity)),
    "meteors_count_per_address_with_rarity.csv",
    "text/csv",
    key='download-csv'
    )

#-------------------------------------------------------
    
    