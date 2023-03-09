
import json
import pandas as pd
import numpy as np
import pymongo
import streamlit as st
import snscrape.modules.twitter as sntwitter

#Streamlit Code 
Header = st.container()

with Header:
    st.title("Welcome to my Twitter Scraping application 🤗")
    st.text("I am using scraper for social networking platforms known as snscrape (SNS). \nIt retrieves objects, such as pertinent posts, \nby scraping things like user profiles, hashtags, or searches.")


keyword = st.sidebar.text_input("Provide a keyword Or an hashtag to begin the search")
Tweet_count = st.sidebar.number_input('Enter the number of tweets to be collected:',min_value=0, max_value=1000)
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")


#twitter Scrapping Code
if st.button("Click to Process"):
    userdata = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + " until:" + str(end_date) + " since:" + str(start_date)).get_items()):
        if i>Tweet_count :
            break  
        userdata.append([tweet.date,tweet.user.id,tweet.url,tweet.content,tweet.renderedContent,tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])
    twitter_Dataset = pd.DataFrame(userdata, columns=['Date','ID','URL','Tweet','Content','User','Reply Count','Retweet Count','Language', 'Source','Like Count'])
    st.dataframe(twitter_Dataset)



# jotw = twitter_Dataset.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False, compression='infer', index=True, indent=None, storage_options=None)
# st.write(jotw)
#CSV download button
st.download_button(label="Download as CSV",data = twitter_Dataset.to_csv(index=False).encode('utf-8'),file_name='Twitterscr_df.csv')

st.download_button(label="Download as json",data = twitter_Dataset.to_json(index=True),file_name='Twitterscr_df.json')






