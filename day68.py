#import libraries
import pandas as pd
#!pip install dash
#dash is the library which helps us create UI of our WebApp.
import dash
import dash_html_components as html
from dash.dependencies import Input, Output

#a very important library for loading your created webpage on your browser
#opens browser, a new tab and performs what has been told to it
import webbrowser

# favicon   =  =  16x16 icon ----> favicon.ico  ----> create an assests folder 
#and store the image there

#declare global variables
project_name = None
var = dash.Dash()

#write your methods
def load_model():
    global load
    load = pd.read_csv('scrappedReviews.csv') 
    
def create_App_UI():
    main_layout = html.Div(
        [
         html.H1(id = 'bb', children = 'AVADA KADAVRA!!!!!!!!!!'),
         html.H5(id = 'cb', children = 'PKMKB'),
         html.Button(id='button', children = 'Submit Here', n_clicks=0)
        ]
    )
    return main_layout

'''
event handling:-if the submit here button is clicked the this method will
update the number of times it has been clicked.

WIRING:--

OBJECT------>-----> EVENT ------>----> FUNCTION
Button------>-----> Click ------>----> tell_noOf_clicks 

Decorators and callback mechanism is a way to implement wiring.
'''
@var.callback(
    Output('cb', 'children'),
    [
     Input('button', 'n_clicks')
    ])


def tell_noOf_clicks(n_clicks):
    print('datatype of nclicks is ',str(type(n_clicks)))   
    print('\nvalue of n_clicks is finally ',str(n_clicks))
    
    if (n_clicks >0):
            return 'X has clicked submit '+str(n_clicks)+' times'
    else:
        return 'Sentiment Analysis with the barberians of Afghan'

def open_browser():
   webbrowser.open_new('http://127.0.0.1:8050/')
   
#main method
def main():
    global project_name
    global load
    global var
    
    load_model()
    open_browser()
    
    print('----------This is the beginning of my project------------')
    project_name = 'Sentiment Analysis with the barberians of Afghan'
    print('\nMy project name is:-- ', project_name)
    #print('Here is our special refernce on the Agenda \'K\' of 19.07.56.001 \n', load.sample(5))
    
    #create basic web application -->
    #title is the title of your html page which is read on the tab 
    var.title = project_name
    #layout is the page layout using all html css tools
    var.layout = create_App_UI()
    #run_server is a very important function which launches the web application on the internet
    #run_server is also a blocking statement it does not allow the next set of code 
    #to be executed until the server is killed(compilation terminated).
    var.run_server()
    
    
    print('\n------|||||||| This is the end of my project ||||||||--------')
    
    project_name = None
    load = None
#call your main method    
if __name__ == '__main__':
    main()
    
    















''' 
# Importing the libraries
import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html
from dash.dependencies import Input, Output


# Declaring Global variables
project_name = None
app = dash.Dash()
# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div(
    [
    html.H1(id='Main_title', children = "Sentiment Analysis with Insights"),
    html.Button(id= 'button_review', children = 'Find Review', n_clicks=0)
    ]    
    )
    
    return main_layout

'''
'''
Event Handling 
When some clicks the button call my method update_app_ui

Wiring 
Object      Event    Function 
Button      Click    update_app_ui

Decorators and callbacks mechanism is a way to implment wiring in python
Input  === Arguments to your callback
Output === return of your callback 

'''
'''
@app.callback(
    Output( 'button_review'   , 'children'     ),
    [
    Input( 'button_review'    ,  'n_clicks'    )
    ]
    )
def update_app_ui(n_clicks):
    
    print("Data Type = ", str(type(n_clicks)))
    print("Value = ", str(n_clicks))
    
    if (n_clicks > 0 ):
        return "Someone has clicked the button = " + str(n_clicks) + " times" 
    else:
        return "Sentiment Analysis with Insights"



# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()
    #update_app_ui()
    
    
    global scrappedReviews
    global project_name
    global app
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', scrappedReviews.sample(5) )
    
    # favicon  == 16x16 icon ----> favicon.ico  ----> assests
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server()
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()
'''    