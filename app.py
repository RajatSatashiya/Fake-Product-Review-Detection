from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import pandas as pd
import sklearn as sk
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import csv

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/fakerev")
def fakerev():
    return render_template("fakerev.html")

@app.route("/predict", methods=['GET','POST'])
def predict():
    dataset = pd.read_csv('datasetfake2.csv')
    ds = dataset[['review','result']]
    ds.loc[ds['result'] == 'CG', 'result'] = 0
    ds.loc[ds['result'] == 'OR', 'result'] = 1

    corpus = []
    for i in range(0, 33892):
      review = re.sub('[^a-zA-Z]', ' ', dataset['review'][i])
      review = review.lower()
      review = review.split()
      ps = PorterStemmer()
      all_stopwords = stopwords.words('english')
      all_stopwords.remove('not')
      review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
      review = ' '.join(review)
      corpus.append(review)

    cv = CountVectorizer()
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    #message = "not a good tv"
    name = request.form.get("name")
    rating = int(request.form.get("rating"))
    message = request.form.get("review")
    #print(message)
    data = [message]
    vect = cv.transform(data).toarray()
    #vect.reshape(np.shape(
    pred = model.predict(vect)
      #classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape))

    if(pred[0] == "CG" and rating >= 3):
        return render_template("fakerev.html", prediction_text=-1)#-1
    else:
        return render_template("fakerev.html", prediction_text=1)#1

@app.route("/spam", methods=['GET', 'POST'])
def spamdetection():
    name = request.form.get("name")
    file = open("datasetSpam.csv")
    reader = csv.reader(file)

    for row in reader:
        if(row[0] == name):
            value = True
            sixtycent = (60 / 100) * int(row[1])
            if(int(row[2]) >= sixtycent):
                value = False
            row2 = {
                "name": row[0],
                "review": row[1],
                "flagged": row[2],
                "year": row[3],
                "value": value
            }    
            return render_template("spam.html", spam_text=row2)
    
    return render_template("spam.html", spam_text=0)#0


if __name__ == "__main__":
    app.run(debug=True)
