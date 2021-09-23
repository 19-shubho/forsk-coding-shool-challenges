import pickle
import pandas as pd
import webbrowser
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

VAR = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
project_name = "Sentiment Analysis with Insights"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

def load_MOD():
    global pickle_model
    global vocab
    global scrappedReviews
    
    
    scrappedReviews = pd.read_csv('scrappedReviews.csv')
    
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    file = open("features.pkl", 'rb') 
    vocab = pickle.load(file)
        
def check_review(reviewText):
    Transf = TfidfTransformer()
    VectLoad = CountVectorizer(decode_error="replace",vocabulary=vocab)
    reviewText = Transf.fit_transform(VectLoad.fit_transform([reviewText]))
    return pickle_model.predict(reviewText)

def create_App_UI():
    global project_name
    main_layout = dbc.Container(
        dbc.Jumbotron(
                [
                    html.H1(id = 'heading', children = project_name, className = 'display-3 mb-4'),
                    dbc.Textarea(id = 'textarea', className="mb-3", placeholder="Enter the Review", value = 'My daughter loves these shoes', style = {'height': '150px'}),
                    dbc.Container([
                        dcc.Dropdown(
                    id='dropdown',
                    placeholder = 'Select a Review',
                    #options=[{'label': i[:100] + "...", 'value': i} for i in scrappedReviews.reviews],
                    options=[{'label': i[:100] + "...", 'value': i} for i in scrappedReviews.reviews],
                    value = scrappedReviews.reviews[0],
                    style = {'margin-bottom': '30px'}
                    
                )
                       ],
                        style = {'padding-left': '50px', 'padding-right': '50px'}
                        ),
                    dbc.Button("Submit", color="dark", className="mt-2 mb-3", id = 'button', style = {'width': '100px'}),
                    html.Div(id = 'result'),
                    html.Div(id = 'result1')
                    ],
                className = 'text-center'
                ),
        className = 'mt-4'
        )
    
    return main_layout

@VAR.callback(
    Output('result', 'children'),
    [
    Input('button', 'n_clicks')
    ],
    [
    State('textarea', 'value')
    ]
    )    
def update_App_UI(n_clicks, textarea):
    result_list = check_review(textarea)
    
    if (result_list[0] == 0 ):
        return dbc.Alert("Negative", color="danger")
    elif (result_list[0] == 1 ):
        return dbc.Alert("Positive", color="success")
    else:
        return dbc.Alert("cannot decipher", color="dark")

@VAR.callback(
    Output('result1', 'children'),
    [
    Input('button', 'n_clicks')
    ],
    [
     State('dropdown', 'value')
     ]
    )
def update_dropdown(n_clicks, value):
    result_list = check_review(value)
    
    if (result_list[0] == 0 ):
        return dbc.Alert("Negative", color="danger")
    elif (result_list[0] == 1 ):
        return dbc.Alert("Positive", color="success")
    else:
        return dbc.Alert("cannot decipher", color="dark")
    
def main():
    global VAR
    global project_name
    load_MOD()
    open_browser()
    VAR.layout = create_App_UI()
    VAR.title = project_name
    VAR.run_server()
    VAR = None
    project_name = None
if __name__ == '__main__':
    main()