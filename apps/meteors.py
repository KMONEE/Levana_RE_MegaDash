import streamlit as st
import plotly
import plotly.express as px
#import statsmodels.api as sm
import pandas as pd
import json


from scrape import scrape_new

def app():

    #st.set_page_config(layout="wide")
    st.title("Meteors")
    st.text ("https://randomearth.io/collections/terra1chrdxaef0y2feynkpq63mve0sqeg09acjnp55v")
    st.text('')

    st.markdown("""
    ---
    """)



    
    meteors = scrape_new('terra1chrdxaef0y2feynkpq63mve0sqeg09acjnp55v')
    st.dataframe(meteors)

    #@st.cache
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
    st.markdown("""## Unique addresses owning Meteors""")

    uniques = meteors['user_addr'].unique()
    st.dataframe(uniques)

    csv2 = convert_df(pd.DataFrame(uniques))

    st.download_button(
    "Press to Download",
    csv2,
    "unique_address_meteors.csv",
    "text/csv",
    key='download-csv'
    )


#-------------------------------------------------------
    
    