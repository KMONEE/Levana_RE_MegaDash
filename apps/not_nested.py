import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json
import ast


def app():

    #st.set_page_config(layout="wide")
    st.title("Dragon Eggs (Not Nested)")
    st.text ("https://randomearth.io/collections/terra1k0y373yxqne22pc9g7jvnr4qclpsxtafevtrpg")
    st.text('')

    st.markdown("""
    ---
    """)


    
    not_nested_df = pd.read_csv('http://165.22.125.123/egg_nfts.csv')
    st.dataframe(not_nested_df)

    #@st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(not_nested_df)

    
    st.download_button(
    "Press to Download",
    csv,
    "not_nested.csv",
    "text/csv",
    key='download-csv'
    )

    st.markdown("""
    ---
    """)

    col1, col2 = st.columns([1,3])


    col1.header("Counts of unnested eggs \n in wallets per rarity")
    rarity_counts = not_nested_df
    rarity_counts['traits'] = rarity_counts['traits'].apply(lambda x: ast.literal_eval(x).get('Rarity'))
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
    col3.markdown("""## Unique addresses owning unnested eggs""")

    uniques = not_nested_df['user_addr'].unique()
    col3.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    col3.download_button(
    "Press to Download",
    csv2,
    "unique_address_egg.csv",
    "text/csv",
    key='download-csv'
    )

    col4.header("""Counts of unnested eggs per wallet""")

    egg_per_wallet = not_nested_df['user_addr'].value_counts().reset_index().rename(columns={'user_addr':'egg_count'})
    col4.dataframe(egg_per_wallet)

    col4.download_button(
    "Press to Download",
    convert_df(pd.DataFrame(egg_per_wallet)),
    "egg_count_per_address.csv",
    "text/csv",
    key='download-csv'
    )

    col5.header("Counts of unnested eggs per wallet w/ rarity")
    egg_per_wallet_rarity = not_nested_df[['user_addr', 'traits']].value_counts().reset_index().rename(columns={'user_addr':'egg_count', 'traits':'rarity', 0:'count'})
    col5.dataframe(egg_per_wallet_rarity)

    col5.download_button(
    "Press to Download",
    convert_df(pd.DataFrame(egg_per_wallet_rarity)),
    "egg_count_per_address_with_rarity.csv",
    "text/csv",
    key='download-csv'
    )

#-------------------------------------------------------
    
    