#importing the libraries -->
import pickle
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output , State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


#declare global variables -->
project_name = None
VAR = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#define functions -->
def load_MOD():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')
  
    global pickle_model
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("features.pkl", 'rb') 
    vocab = pickle.load(file)

def check_review(reviewText):

    #reviewText has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model preidctor
    #load it later......................

    Transf = TfidfTransformer()
    VectLoad = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorise_REVIEW = Transf.fit_transform(VectLoad.fit_transform([reviewText]))


    # add code to test the sentiment of using both the model
    # 0 == negative  , 1 == positive...........................
    
    return pickle_model.predict(vectorise_REVIEW)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_App_UI():
    main_layout = html.Div(
    [
    html.H1(id='focus_title', children = "Sentiment Analysis with Insights"),
    
    dcc.Textarea(
        id = 'getParameter',
        placeholder = 'Enter review here.....',
        style = {'width':'100%', 'height':100}
        ),
    
    dbc.Button(
        children = 'Find Review',
        id = 'button_review',
        color = 'dark',
        style= {'width':'100%'}
        ),
    
    html.H1(children = None, id='result')
    
    ]    
    )
    
    return main_layout


'''
@VAR.callback(
    Output('result', 'children'),
    [
    Input('getParameter',  'value')
    ]
    )
def update_App_UI(getParameter):
    
    print("data type = ", str(type(getParameter)))
    print("value is = ", str(getParameter))

    response = check_review(getParameter)

    if (response[0] == 0):
        result = 'Negative'
    elif (response[0] == 1 ):
        result = 'Positive'
    else:
        result = 'cannot decipher'

    return result
'''


@VAR.callback(
    Output('result' , 'children'),
    [
    Input('button_review' , 'n_clicks')
    ],
    [
    State('getParameter' ,'value')
    ]
    )
def MODIFY_UI(n_clicks, getParameter):

    print("data type = ", str(type(n_clicks)))
    print("value is = ", str(n_clicks))


    print("data type = ", str(type(getParameter)))
    print("value is = ", str(getParameter))


    if (n_clicks > 0):

        response = check_review(getParameter)
        if (response[0] == 0):
            result = 'Negative'
        elif (response[0] == 1 ):
            result = 'Positive'
        else:
            result = 'cannot decipher'
        
        return result
        
    else:
        return ""


#define main -->
def main():
    print("----------This is the beginning of my project------------")
    load_MOD()
    open_browser()
    #update_App_UI()
    
    
    global scrappedReviews
    global project_name
    global VAR
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', scrappedReviews.sample(5) )
    
    # favicon  == 16x16 icon ----> favicon.ico  ----> assests
    VAR.title = project_name
    VAR.layout = create_App_UI()
    VAR.run_server()
    
    
    
    print("------|||||||| This is the end of my project ||||||||--------")
    project_name = None
    scrappedReviews = None
    VAR = None
    
        
#call your main -->
if __name__ == '__main__':
    main()
    
    
    