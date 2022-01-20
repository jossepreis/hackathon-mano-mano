
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
    st.image(image1,)
  

    
    
    file_ = open("manamanoreduit.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" >',
    unsafe_allow_html=True,)
    

    st.write('--------------------------------------------------------------------------')
  
 

    st.markdown("<h1 style='text-align: center; color: black;'>Frais de port, freins à l'achat ?</h1>", unsafe_allow_html=True)
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    
    
    
    audio_file = open('Mahna Mahna (mais Non Mais Non) (radio Edit) Free Download  (hearthis.at).mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
    


    
    
def page1():
    
    st.markdown("<h1 style='text-align: center; color: black;'>Titre page 1</h1>", unsafe_allow_html=True)
    
    st.write ('-----------------------------------------------------------')




def page2():
    
    
    st.markdown("<h1 style='text-align: center; color: black;'>Titre page 2</h1>", unsafe_allow_html=True)
    
    st.write ('-----------------------------------------------------------')




def page3():
    
    
    st.markdown("<h1 style='text-align: center; color: black;'>Titre page 3</h1>", unsafe_allow_html=True)
    
    st.write ('-----------------------------------------------------------')



    
    
if __name__ == "__main__":
    main()

