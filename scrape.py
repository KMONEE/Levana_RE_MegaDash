import pandas as pd
import json
import cloudscraper
import time
def scrape_new(collection_address):
    final_df = pd.DataFrame()
    scraper = cloudscraper.create_scraper()
    max_page = json.loads(scraper.get(f"https://randomearth.io/api/items?collection_addr={collection_address}&page=99999").text)['pages']
    for page in range(1, max_page+1):
        counter = 0
        while counter != 1:
            try:
                #pd.read_csv(f'{csv_name}.csv')
                page_data = scraper.get(f"https://randomearth.io/api/items?collection_addr={collection_address}&page={page}").text
                
                #pd.DataFrame.from_dict(json.loads(page_data)['items'])

                final_df = pd.concat([final_df, pd.DataFrame.from_dict(json.loads(page_data)['items'])])
                #final_df.to_csv(f'{csv_name}.csv', index=False)
                time.sleep(.20) #yeah yeah it's not efficient, sue me!
                counter += 1
            except Exception as e:
                print(page)
                time.sleep(3)
                pass
    return final_df