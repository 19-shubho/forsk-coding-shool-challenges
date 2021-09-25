# Importing the libraries
import pickle
import pandas as pd
import webbrowser
# !pip install dash
import dash
from dash import html
from dash import dcc 
import dash_bootstrap_components as dbc
from matplotlib import pyplot as plt

from dash.dependencies import Input, Output , State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import os
import wordcloud
from collections import Counter
import numpy as np
from wordcloud import WordCloud, STOPWORDS

# Declaring Global variables
project_name = None
VAR = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Defining My Functions
def LD_MOD():
    global SCRAP_revITEM
    SCRAP_revITEM = pd.read_csv('ScrapRev11.csv')
    
  
    global pickle_model
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("features.pkl", 'rb') 
    vocab = pickle.load(file)
    #PIE CHART
    print('Loading Data......')
    temp = []
    for i in SCRAP_revITEM['reviews']:
        temp.append(chk_REV(i)[0])
    SCRAP_revITEM['sentiment'] = temp
    
    POS = len(SCRAP_revITEM[SCRAP_revITEM['sentiment']==1])
    NEG = len(SCRAP_revITEM[SCRAP_revITEM['sentiment']==0])
    
    explode = (0.1,0)  

    langs = ['POS', 'NEG',]
    students = [POS,NEG]
    colors = ['#1cbdfc','red']
    plt.pie(students,explode=explode,startangle=90,colors=colors, labels = langs,autopct='%1.2f%%')
    cwd = os.getcwd()
    if 'assets' not in os.listdir(cwd):
        os.makedirs(cwd+'/assets')
    plt.savefig('assets/sentiment.png')
    #wordcloud
    DS = SCRAP_revITEM['reviews'].to_list()
    str1 = ''
    for i in DS:
        str1 = str1+i
    str1 = str1.lower()

    stopwords = set(STOPWORDS)
    cloud = WordCloud(width = 800, height = 400,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(str1)
    cloud.to_file("assets/WC.png")
    #drop down
    global get_droppedValues
    get_droppedValues = {}
    for i in range(400,501):
        get_droppedValues[SCRAP_revITEM['reviews'][i]] = SCRAP_revITEM['reviews'][i]
    get_droppedValues = [{"label":key, "value":values} for key,values in get_droppedValues.items()]
    
def chk_REV(Cust_Statemnt):

    #Cust_Statemnt has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model preidctor
    #load it later

    Transf = TfidfTransformer()
    VectLoad = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorise_REVIEW = Transf.fit_transform(VectLoad.fit_transform([Cust_Statemnt]))


    # Add code to test the sentiment of using both the model
    # 0 == NEG   1 == POS
    
    return pickle_model.predict(vectorise_REVIEW)

def BOOT_Browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_App_UI():
    main_layout = html.Div(
    [
    html.H1(id='focus_TITLE', children = "SENTIMENT ANALYSIS WITH INSIGHTS",style={'text-align':'center', 'font-family':'Lucida Handwriting','background-color':'#DC143C'}),
    html.Hr(style={'background-color':'#DC143C','border':'0rem'}),
    
    html.H2(children = "PIE CHART",style = {'text-align':'center','font-weight':'bold', 'font-family':'Times New Roman', 'text-decoration':'underline','background-color':'#D2B48C'}),
    
   
    html.P([html.Img(src=VAR.get_asset_url('sentiment.png'),style={'width':'700px','height':'410px'})],style={'text-align':'center','background-color':'#FFB6C1'}),
   
    html.Hr(style={'background-color':'#A0522D'}),
   
    html.H2(children = "WORD CLOUD",style = {'text-align':'center','font-weight':'bold','font-family':'Times New Roman', 'text-decoration':'underline','background-color':'#de0d4c'}),
   
    html.P([html.Img(src=VAR.get_asset_url('WC.png'),style={'width':'95%','height':'410px'})],style={'text-align':'center','background-color':'#FFB6C1'}),
   
    html.Hr(style={'background-color':'#C71585'}),
   
    html.H2(children = "Select a Review",style = {'text-align':'center', 'font-family':'Cursive', 'text-decoration':'underline','text-shadow': '2px 2px 5px red','background-color':'#FFB6C1'}),
    
    dcc.Dropdown(
                id='CT_DD', 
                  options=get_droppedValues,
                  placeholder = 'Select a Review',style={'font-size':'22px', 'font-family':'Courier New', 'height':'75px'}
                    ),
    
    html.H1(children = 'Enter your REVIEW!!!',id='sentiment1',style={'text-align':'center',  'font-family':'Courier New','background-color':'#ADFF2F'}),
    
    html.Hr(style={'background-color':'#90EE90'}),
    
    html.H2(children = "Find Sentiment of Your Review",style = {'text-align':'center', 'font-family':'Cursive', 'text-decoration':'underline','text-shadow': '2px 2px 5px red','background-color':'#FFB6C1'}),
    
    dcc.Textarea(
        id = 'getParameter',
        placeholder = 'Enter the review here.....',
        style = {'width':'100%', 'height':155, 'font-size':'22px', 'font-family':'Courier New'}
        ),
    
    dbc.Button(
        children = 'Find Review',
        id = 'ButtREV',
        color = 'dark',
        style= {'width':'100%','text-shadow': '2px 2px 5px red','font-family':'Courier New'}
        ),
    
    html.H1(children = 'Enter your REVIEW!!!', id='result',style={'text-align':'center', 'font-family':'Courier New','background-color':'#ADFF2F'})
    
    ]    
    )
    
    return main_layout



'''
@VAR.callback(
    Output( 'result'   , 'children'     ),
    [
    Input( 'getParameter'    ,  'value'    )
    ]
    )
def create_App_UI(getParameter):
    
    print("data type is:--  = ", str(type(getParameter)))
    print("value is:-- = ", str(getParameter))

    response = chk_REV(getParameter)

    if (response[0] == 0):
        result = 'NEG'
    elif (response[0] == 1 ):
        result = 'POS'
    else:
        result = 'could not decipher'

    return result
'''


@VAR.callback(
    Output( 'result'   , 'children'     ),
    [
    Input( 'ButtREV'    ,  'n_clicks')
    ],
    [
    State( 'getParameter'  ,   'value'  )
    ]
    )
def MODIFY_UI(n_clicks, getParameter):

    print("data type is:--  = ", str(type(n_clicks)))
    print("value is:-- = ", str(n_clicks))


    print("data type is:--  = ", str(type(getParameter)))
    print("value is:-- = ", str(getParameter))


    if (n_clicks > 0):

        response = chk_REV(getParameter)
        if (response[0] == 0):
            result = 'NEGATIVE'
        elif (response[0] == 1 ):
            result = 'POSITIVE'
        else:
            result = 'could not decipher'
        
        return result
        
    else:
        return ""

@VAR.callback(
    Output("sentiment1", "children"),
    [Input("CT_DD", "value")])
def TELL_SENTI(review1):
    sentiment = []
    if review1:
        if chk_REV(review1)==0:
            sentiment='NEGATIVE' 
        if chk_REV(review1)==1:
            sentiment='POSITIVE'
    else:
        sentiment='Enter your REVIEW!!!'
    return sentiment
# Main Function to control the Flow of your Project
def main():
    print("-----<| | | |  Start of your project  | | | |>-----")
    LD_MOD()
    BOOT_Browser()
    #create_App_UI()
    
    
    global SCRAP_revITEM
    global project_name
    global VAR
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', SCRAP_revITEM.sample(5) )
    
    # favicon  == 16x16 icon ----> favicon.ico  ----> assests
    VAR.title = project_name
    VAR.layout = create_App_UI()
    VAR.run_server(host='0.0.0.0')
    
    
    
    print("-----<| | | |  End of my project  | | | |>-----")
    project_name = None
    SCRAP_revITEM = None
    VAR = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()