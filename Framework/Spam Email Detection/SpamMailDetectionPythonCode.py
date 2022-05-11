# -*- coding: utf-8 -*-

import pandas as pd
import re
import nltk
import sys
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

messages = pd.read_csv('D:\Programming and Certifications\Research Paper\End-to-End Invoice Processing\Data\Temp\ModelTrainingDataset', sep='\t', names=["label", "message"])

ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    tempMessage = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    tempMessage = tempMessage.lower()
    tempMessage = tempMessage.split()
    tempMessage = [ps.stem(word) for word in tempMessage if not word in stopwords.words('english')]
    tempMessage = ' '.join(tempMessage)
    corpus.append(tempMessage)

cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

spam_detect_model = MultinomialNB().fit(X_train, y_train)
y_pred=spam_detect_model.predict(X_test)

confusion_m = confusion_matrix(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)













input_mail = str(sys.argv[1])
#input_mail = "congrats on winning the 5 crore lottery"
df=pd.DataFrame([input_mail],columns=['message'])

corpus=[]

for i in range(0,len(df)):
    tempMessage=re.sub('[^a-zA-Z]',' ',df['message'][i])
    tempMessage=tempMessage.lower()
    tempMessage=tempMessage.split()
    tempMessage=[ps.stem(word) for word in tempMessage if word not in stopwords.words('english')]
    tempMessage=' '.join(tempMessage)
    corpus.append(tempMessage)

df=cv.transform(corpus).toarray()

pred=spam_detect_model.predict(df)

label=pred[0]

if label==1:
    text_file = open("D:\Programming and Certifications\Research Paper\End-to-End Invoice Processing\Data\Temp\PredictionFile.txt", "w")
    text_file.write('Spam mail')
    print('spam')
    text_file.close()
else:
    text_file = open("D:\Programming and Certifications\Research Paper\End-to-End Invoice Processing\Data\Temp\PredictionFile.txt", "w")
    text_file.write('Ham mail')
    print('ham')
    text_file.close()
