import pandas as pd
import numpy as np
import nltk
import string
from sklearn.metrics import accuracy_score
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from prefect import task, flow

@task
def load_data(file_path):
    
    return pd.read_csv(file_path)
@task
def split_input_output(data,input,output):
    
    X = data[input]
    y= data[output]
    
    return X,y
@task 
def split_train_test(X,y,test_size=0.25,random_state=0):
    
    return train_test_split(X,y,test_size=test_size,random_state=random_state)

lemmatizer = WordNetLemmatizer()

@task
def clean_data(doc):
    doc = doc.replace("READ"," ")
    
    #Remove punctuation and numbers
    doc = "".join([char for char in doc if char not in string.punctuation and not char.isdigit()])
    doc = doc.lower()
    #Tokenization
    tokens = nltk.word_tokenize(doc)
    
    lemmatized_tokens = [lemmatizer.lemmatize(tokens) for token in tokens]
    stop_words = set(stopwords.words('english'))
    
    filtered_tokens = [words for words in lemmatized_tokens if words.lower() not in stop_words]
    
    return " ".join(filtered_tokens)

vectorize = CountVectorizer()

@task
def preprocess_data(X_train,X_test):
    X_train = vectorize.fit_transform(X_train)
    X_test = vectorize.transform(X_test)
    
    return X_train,X_test

@task
def train_model(X_train,y_train):
    clf = MultinomialNB()
    clf.fit(X_train,y_train)
    
    return clf

@task
def evaluate_model(model,X_train,y_train,X_test,y_test):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    train_score = accuracy_score(X_train,y_train_pred)
    test_score = accuracy_score(y_test,y_test_pred)
    return train_score , test_score

@flow
def workflow():
    path = "data.csv"
    
    input = ['Review text']
    output = 'Ratings'
   
    #load data
    data=load_data(path)
  
   
    
    #identify inputs and outputs
    X,y  = split_input_output(data,input,output)
    
    #split data into train and test
    X_train,X_test,y_train,y_test = split_train_test(X,y)
    
    # data cleaning
    X_train = clean_data(X_train)
    X_test = clean_data(X_test)
    
    #data preprocessing
    X_train, y_train = preprocess_data(X_train,X_test)
    
    # Build a model
    model = train_model(X_train,y_train)
    
    #evaluate_model
    
    train_score,test_score= evaluate_model(model,X_train,y_train,X_test,y_test)
    
    print("Train Score:", train_score)
    print("Test Score:", test_score)
    

if __name__ == "__main__":
    workflow.serve(
        name ='Sentiment Prediction',
        cron ="* * * * *"
    )
    

