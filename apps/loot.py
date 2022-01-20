import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json


from scrape import scrape_new

def app():

    #st.set_page_config(layout="wide")
    st.title("Loot")
    st.text ("https://randomearth.io/collections/terra14gfnxnwl0yz6njzet4n33erq5n70wt79nm24el")
    st.text('')

    st.markdown("""
    ---
    """)



    
    loot = scrape_new('terra14gfnxnwl0yz6njzet4n33erq5n70wt79nm24el')
    st.dataframe(loot)

    #@st.cache
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
    rarity_counts['traits'] = rarity_counts['traits'].apply(lambda x: x.get('Rarity'))
    #rarity_counts['traits'] = rarity_counts['traits'].apply(lambda x: ast.literal_eval(x).get('Rarity'))
    rarity_counts = rarity_counts['traits'].value_counts()
    #st.dataframe(rarity_counts)
    col1.dataframe(rarity_counts)


    df = pd.DataFrame(rarity_counts)
    fig = px.pie(df, values='traits', names=df.index)
    col2.plotly_chart(fig, use_column_width=True)

    

    st.markdown("""
    ---
    """)
    st.markdown("""## Unique addresses owning Loot""")

    uniques = loot['user_addr'].unique()
    st.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    st.download_button(
    "Press to Download",
    csv2,
    "unique_address_loot.csv",
    "text/csv",
    key='download-csv'
    )


#-------------------------------------------------------
    
    