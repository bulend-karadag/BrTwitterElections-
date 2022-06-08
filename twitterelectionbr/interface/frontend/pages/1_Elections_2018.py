import streamlit as st
import numpy as np
from components.bootstrap import card
from static.core_css import main_css
from PIL import Image
import os

Title_html = """
    <style>
        h3{
          font-size: 16px;
          color: #2E2E2E;
          text-align: center;
          font-style: oblique;
          font-weight: bold;

    </style> """


def main():
    st.set_page_config(layout="wide")
    st.markdown(Title_html, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color:#2E2E2E ;'>Twiitter Sentiment Analysis</h1>", unsafe_allow_html=True)
    #WRITE THE CODE BELOW
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center; color: #FD2B49;'>Fernando Haddad</h1>", unsafe_allow_html=True)
        rel_path = '../static/haddad_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Haddad by the types of sentiments', use_column_width='auto')
        st.markdown("<h3>Numbers of tweet written for Haddad by the types of sentiments</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption="Daily numbers of tweet written for Haddad", use_column_width='auto')
        
        rel_path = '../static/haddad_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        
        rel_path = '../static/haddad_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Haddad', use_column_width='auto')
        
        rel_path = '../static/haddad_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        
        rel_path = '../static/haddad_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        
        rel_path = '../static/haddad_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        
        rel_path = '../static/haddad_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        
        rel_path = '../static/haddad_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Haddad', use_column_width='auto')
        
        rel_path = '../static/haddad_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Haddad', use_column_width='auto')


    with col2:
        st.markdown("<h1 style='text-align: center; color: #279A55;'>Jair Bolsonaro</h1>", unsafe_allow_html=True)
        rel_path = '../static/bolsonaro_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Bolsonaro by the types of sentiments', use_column_width='auto')
        st.markdown("<h3>Numbers of tweet written for Bolsonaro by the types of sentiments</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily numbers of tweet written for Bolsonaro', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Bolsonaro', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Bolsonaro', use_column_width='auto')
        
        rel_path = '../static/bolsonaro_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Bolsonaro', use_column_width='auto')

main()
