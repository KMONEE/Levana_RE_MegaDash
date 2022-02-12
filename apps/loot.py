import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json
import ast



def app():

    #st.set_page_config(layout="wide")
    st.title("Loot")
    st.text ("https://randomearth.io/collections/terra14gfnxnwl0yz6njzet4n33erq5n70wt79nm24el")
    st.text('')

    st.markdown("""
    ---
    """)



    
    loot = pd.read_csv('http://165.22.125.123/loot_nfts.csv')
    st.dataframe(loot)

    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(loot)

    
    st.download_button(
    "Press to Download",
    csv,
    "loot.csv",
    "text/csv",
    key='download-csv'
    )

    st.markdown("""
    ---
    """)

    col1, col2 = st.columns([1,3])


    col1.header("Counts of Loot NFTs \n in wallets per rarity")
    rarity_counts = loot
    rarity_counts['traits'] = rarity_counts['traits'].apply(lambda x: ast.literal_eval(x).get('Faction')) #this is used to convert the DataFrame column to readable json
    rarity_counts = rarity_counts['traits'].value_counts()
    col1.dataframe(rarity_counts)


    df = pd.DataFrame(rarity_counts)
    fig = px.pie(df, values='traits', names=df.index)
    col2.plotly_chart(fig, use_column_width=True)

    

    st.markdown("""
    ---
    """)
    
    col3, col4, col5 = st.columns([1,1,1])
    col3.markdown("""## Unique addresses owning loot (talisman)""")

    uniques = loot['user_addr'].unique()
    col3.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    col3.download_button(
    "Press to Download",
    csv2,
    "unique_address_loot.csv",
    "text/csv",
    key='download-csv'
    )

    col4.header("""Counts of loot (talisman) per wallet""")

    loot_per_wallet = loot['user_addr'].value_counts().reset_index().rename(columns={'user_addr':'loot_count'})
    col4.dataframe(loot_per_wallet)

    col4.download_button(
    "Press to Download",
    convert_df(pd.DataFrame(loot_per_wallet)),
    "loot_count_per_address.csv",
    "text/csv",
    key='download-csv'
    )

    col5.header("Counts of loot (talisman) per wallet w/ rarity")
    loot_per_wallet_rarity = loot[['user_addr', 'traits']].value_counts().reset_index().rename(columns={'user_addr':'loot_count', 'traits':'rarity', 0:'count'})
    col5.dataframe(loot_per_wallet_rarity)

    col5.download_button(
    "Press to Download",
    convert_df(pd.DataFrame(loot_per_wallet_rarity)),
    "loot_count_per_address_with_rarity.csv",
    "text/csv",
    key='download-csv'
    )


#-------------------------------------------------------
    
    