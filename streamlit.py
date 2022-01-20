
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

df_august = pd.read_csv('2022-01 Wild Code School x ManoMano_ CES Data Set.xlsx - August 2021.csv',low_memory = False)
df_september = pd.read_csv('2022-01 Wild Code School x ManoMano_ CES Data Set.xlsx - September 2021.csv',low_memory = False)
df_october = pd.read_csv('2022-01 Wild Code School x ManoMano_ CES Data Set.xlsx - October 2021.csv',low_memory = False)
df_november = pd.read_csv('2022-01 Wild Code School x ManoMano_ CES Data Set.xlsx - November 2021.csv',low_memory = False)
df_complet_clean = pd.read_csv('csv_hackathon_2.csv',low_memory=False)
# Pivot table
df_family_fee_avg=pd.pivot_table(data=df_complet_clean, index='family', values=['shipping_fees','ratio'], aggfunc='mean').reset_index()
df_category_fee_avg=pd.pivot_table(data=df_complet_clean, index='category', values=['shipping_fees','ratio'], aggfunc='mean').reset_index()

def main():
    
    pages = {
        'Homepage': homepage,
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
  
 

    st.markdown("<h3 style='text-align: center; color: black;'>Shipping costs: major barrier to e-commerce purchases?</h3>", unsafe_allow_html=True)
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




    list_dict = []
    for i in range(0,7):
        df_score = df_complet_clean[df_complet_clean['score']==i]
        dict_score = {}
        for col in df_score.columns[-16:-6]:
            dict_score[col]=df_score[col].value_counts()[1]
        list_dict.append(dict_score)

    dict_score = {}
    for col in df_complet_clean.columns[-16:-6]:
        dict_score[col]=df_complet_clean[col].value_counts()[1]

    fig2 = px.pie(data_frame=df_complet_clean, names='score',color_discrete_sequence=px.colors.qualitative.Plotly)

    fig2.update_traces(textposition='inside')
    fig2.update_layout(template='seaborn', title='distribution of CES score' ,height = 800,width=500)
    st.plotly_chart (fig2,use_container_width=True)
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')



    fig = make_subplots(
    rows=4, cols=2,
    subplot_titles=('total', 'score = 0','score = 1','score = 2','score = 3','score = 4','score = 5','score = 6'),
    )


    fig.append_trace(
        go.Bar(x=list(dict_score.keys()),
        y=list(dict_score.values()),
        marker_color=px.colors.qualitative.Plotly),
        row=1, col=1
)

    fig.append_trace(
        go.Bar(x=list(list_dict[0].keys()),
        y=list(list_dict[0].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=1, col=2
)

    fig.append_trace(
        go.Bar(x=list(list_dict[1].keys()),
        y=list(list_dict[1].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=2, col=1
)

    fig.append_trace(
        go.Bar(x=list(list_dict[2].keys()),
        y=list(list_dict[2].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=2, col=2
)

    fig.append_trace(
        go.Bar(x=list(list_dict[3].keys()),
        y=list(list_dict[3].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=3, col=1
)

    fig.append_trace(
        go.Bar(x=list(list_dict[4].keys()),
        y=list(list_dict[4].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=3, col=2
)

    fig.append_trace(
        go.Bar(x=list(list_dict[5].keys()),
        y=list(list_dict[5].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=4, col=1
)

    fig.append_trace(
        go.Bar(x=list(list_dict[6].keys()),
        y=list(list_dict[6].values()),
        marker_color=px.colors.qualitative.Plotly),
        row=4, col=2
)

    fig.update_layout(template='seaborn', title='reasons of bad CES score' ,showlegend=False,height = 1250,width=1000)
    st.plotly_chart (fig,use_container_width=True)







def page2():


    st.markdown("<h1 style='text-align: center; color: black;'>Titre page 2</h1>", unsafe_allow_html=True)
    
    fig3 = make_subplots(rows=1, cols=1)

    fig3.add_trace(go.Scatter(x=df_family_fee_avg['family'], y=df_family_fee_avg['shipping_fees'], mode='lines', name= 'Avg. Shipping Fees'), row=1, col=1)
    fig3.add_trace(go.Scatter(x=df_family_fee_avg['family'], y=df_family_fee_avg['ratio'], mode='lines', name= 'Avg. Ratio of SF on Total'), row=1, col=1)
    fig3.update_layout(title='Shipping Fees vs Family',xaxis_title='Family',height = 600,width=1200)
    st.plotly_chart (fig3,use_container_width=True)
    
    
    st.write ('-----------------------------------------------------------')


    fig4 = make_subplots(rows=1, cols=1)

    fig4.add_trace(go.Scatter(x=df_category_fee_avg['category'], y=df_category_fee_avg['shipping_fees'], mode='lines', name= 'Avg. Shipping Fees'), row=1, col=1)
    fig4.add_trace(go.Scatter(x=df_category_fee_avg['category'], y=df_category_fee_avg['ratio'], mode='lines', name= 'Avg. Ratio of SF on Total'), row=1, col=1)
    fig4.update_layout(title='Shipping Fees vs Category',
                   xaxis_title='Category')
    st.plotly_chart (fig4,use_container_width=True)



def page3():
    
    
    st.markdown("<h1 style='text-align: center; color: black;'>Titre page 3</h1>", unsafe_allow_html=True)
    
    st.write ('-----------------------------------------------------------')



    
    
if __name__ == "__main__":
    main()

