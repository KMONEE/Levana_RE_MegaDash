import streamlit as st
from PIL import Image

import pandas as pd
import json



from multiapp import MultiApp
#from apps import home, not_nested, nested, loot, meteor, meteor_dust # import your app modules here
from apps import home, loot, nested, meteor_dust, meteors, not_nested, stats

app = MultiApp()

st.set_page_config(layout="wide")
#levana = Image.open("levana.png")
#st.image(levana)

st.markdown("""
# Levana NFT Tracking
""")


#st.write("""Right now this dashboard is scraping the RandomEarth API each time a page on the dashboard is opened. It can take up to 15min to generate a page but it usually does not take so long.""")
#st.markdown("""## Scraping occurs each time a page is opened, results are not cached.""")
#st.markdown("""## Downloads will cause the page to reload and the scrape to restart.""")



# Add all your application here
app.add_app("Home", home.app)
app.add_app("--> STATS <--", stats.app)
app.add_app("Loot", loot.app)
app.add_app("Dragon Eggs (Not Nested)", not_nested.app)
app.add_app("Dragon Eggs (Nested)", nested.app)
app.add_app("Meteors", meteors.app)
app.add_app("Meteor Dust", meteor_dust.app)



# The main app
app.run()