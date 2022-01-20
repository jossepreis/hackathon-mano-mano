
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


    st.write ('-----------------------------------------------------------')

    st.markdown('')


    
    st.write ('-----------------------------------------------------------')

    st.markdown('s')
    
    
    st.markdown ('C')

    
    
def page1():
    
    st.markdown ('page 1')
    
    st.write ('-----------------------------------------------------------')

    st.markdown('')

        
    st.markdown ('')

def page2():
    
    
    st.markdown ('page 1')
    
    st.write ('-----------------------------------------------------------')

    st.markdown('')

        
    st.markdown ('')


def page3():
    
    
    st.markdown ('page 1')
    
    st.write ('-----------------------------------------------------------')

    st.markdown('')

        
    st.markdown ('')

    
    
if __name__ == "__main__":
    main()

