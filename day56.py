import pandas as pd
dataset = pd.read_csv('movie.csv')

# Cleaning the texts
import re
import nltk

nltk.download('stopwords')
    
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


CORPUS = []
for i in range(0, dataset.shape[0]):
    rev = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    rev = rev.lower()
    rev = rev.split()
    ps = PorterStemmer()
    rev = [ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
    rev = ' '.join(rev)
    CORPUS.append(rev)


# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 4000)
feat = cv.fit_transform(CORPUS).toarray()

lab = dataset.iloc[:, 0].values


from sklearn.preprocessing import LabelEncoder
labEncod = LabelEncoder()
lab = labEncod.fit_transform(lab)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split as TTS
featTrain, featTest, labTrain, labTest = TTS(feat, lab, test_size = 0.25, random_state = 0)




from sklearn.linear_model import LogisticRegression

model  = LogisticRegression()

model.fit(featTrain, labTrain)

# Predicting the Test set results
predLabels = model.predict(featTest)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labTest, predLabels)

score = accuracy_score(labTest,predLabels)

print ("model accuracy is : "+str(round(score*100, 2))+"%")