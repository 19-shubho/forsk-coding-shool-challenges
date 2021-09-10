import numpy as np
import pandas as pd

dataset = pd.read_csv("affairs.csv")

# Separating data into Independent and Dependent Variables
feat = dataset.iloc[:,:-1].values
lab = dataset.iloc[:,-1].values

def Model(feat, lab):
    # Applying OneHotEncoding
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    
    colOHE = [6,7]  # Columns to be OneHotEncoded
    ct = ColumnTransformer([("encoder", OneHotEncoder(), [6,7])], remainder = 'passthrough')
    feat = ct.fit_transform(feat)
    
    # Getting indexes for the columns to be dropped, to avoid dummy variable trap
    totCol, indexes = 0, []
    for col in colOHE:
        uniqValCnt = len(dataset.iloc[:,col].value_counts())
        totCol += uniqValCnt
        indexes.append(totCol - uniqValCnt)
    
    # Dropping the dummy variable trap columns
    feat = np.delete(feat, indexes, axis=1)
    
    # Splitting the dataset into train and test
    from sklearn.model_selection import train_test_split as TTS
    
    featTrain,featTest,labTrain,labTest = TTS(feat, lab, test_size = 0.25,
                                        random_state = 0)
    
    # Logistic Regression Model
    from sklearn.linear_model import LogisticRegression
    obj = LogisticRegression(random_state=0)
    obj.fit(featTrain, labTrain)
    
    pred = obj.predict(featTest)   # Prediction on test data
    
    # Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(labTest, pred)
    
    # check the accuracy on the Model
    scoreModel = obj.score(featTest, labTest)
    
    # Preprocessing the new individual's data
    """
     She's a 25-year-old teacher who graduated college, 
     has been married for 3 years, 
     has 1 child, 
     rates herself as strongly religious, 
     rates her marriage as fair, 
     and her husband is a farmer.
        
    """
    val = np.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1,-1)
    val = ct.transform(val)
    val = np.delete(val, indexes, axis=1)
    
    valPred = obj.predict_proba(val)  # Predicting Individual's value
    

    
    return pred, cm, scoreModel,valPred


Pred, cm, Score, valPred = Model(feat,lab)

print ("model accuracy using confusion matrix : "+str(cm))
print ("model accuracy using .score() function : "+str(round(Score*100,2)))
print ("percentage of total women actually had an affair : "+str(round(dataset["affair"].mean()*100,2))+"%")
print ("probability of an affair for a random woman is : "+str(valPred))
