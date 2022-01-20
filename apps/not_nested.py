import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json


from scrape import scrape_new

def app():

    #st.set_page_config(layout="wide")
    st.title("Dragon Eggs (Not Nested)")
    st.text ("https://randomearth.io/collections/terra1k0y373yxqne22pc9g7jvnr4qclpsxtafevtrpg")
    st.text('')

    st.markdown("""
    ---
    """)



    #not_nested_df = pd.read_csv(r'C:\Users\Admin\Documents\work\LEVANA\Levana NFT dashboard\Levana_RE_MegaDash\not_nested.csv')
    
    not_nested_df = scrape_new('terra1k0y373yxqne22pc9g7jvnr4qclpsxtafevtrpg')
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
    st.markdown("""## Unique addresses owning eggs""")

    uniques = not_nested_df['user_addr'].unique()
    st.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    st.download_button(
    "Press to Download",
    csv2,
    "unique_address_not_nested.csv",
    "text/csv",
    key='download-csv'
    )


#-------------------------------------------------------
    
    