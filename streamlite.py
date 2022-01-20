
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import nltk
nltk.download(["names","stopwords","state_union","twitter_samples","movie_reviews","averaged_perceptron_tagger","vader_lexicon","punkt" ])
from PIL import Image   
import base64

def main():
    
    pages = {
        'Accueil': homepage,
        'Page 1': page1,
        'Page 2': page2,
        'Page 3': page3}

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Home'
        })

    with st.sidebar:
        page = st.selectbox("", tuple(pages.keys()))

    pages[page]()



def homepage():
    st.markdown('')
    image1 = Image.open('Mano-Manon-new-logo.png')
    st.image(image1,caption='https://www.manomano.fr/')

    
    
    
    
    file_ = open("default.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,)
    

    st.markdown('')


    
   
    st.markdown('')
    
    
    st.markdown ('')

    
    
def page1():
    
    st.markdown ('page 1')
    
    st.write ('-----------------------------------------------------------')

    st.markdown('')

        
    st.markdown ('')

def page2():
    
    
    st.markdown ('page 2')
    
    st.write ('-----------------------------------------------------------')

    st.markdown('')

        
    st.markdown ('')


def page3():
    
    
    st.markdown ('page 3')
    
    st.write ('-----------------------------------------------------------')

    st.markdown('')

        
    st.markdown ('')

    
    
if __name__ == "__main__":
    main()

