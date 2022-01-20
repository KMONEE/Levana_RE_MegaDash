import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json
import ast


from scrape import scrape_new

def app():

    #st.set_page_config(layout="wide")
    st.title("Nested Dragon Eggs")
    st.text ("https://randomearth.io/collections/terra1vhuyuwwr4rkdpez5f5lmuqavut28h5dt29rpn6")
    st.text('')

    st.markdown("""
    ---
    """)



    
    nested_df = scrape_new('terra1vhuyuwwr4rkdpez5f5lmuqavut28h5dt29rpn6')
    st.dataframe(nested_df)

    #@st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(nested_df)

    
    st.download_button(
    "Press to Download",
    csv,
    "nested.csv",
    "text/csv",
    key='download-csv'
    )

    st.markdown("""
    ---
    """)

    col1, col2 = st.columns([1,3])


    col1.header("Counts of nested eggs \n in wallets per rarity")
    rarity_counts = nested_df
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
    st.markdown("""## Unique addresses owning nested eggs""")

    uniques = nested_df['user_addr'].unique()
    st.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    st.download_button(
    "Press to Download",
    csv2,
    "unique_address_nested.csv",
    "text/csv",
    key='download-csv'
    )


#-------------------------------------------------------
    
    