#Feature Extraction and Vectorization
import numpy as np
import pandas as pd
import pickle
train = pd.read_csv("refine.csv", header=0)
#print train.shape
#print train.columns.values
from sklearn.feature_extraction.text import CountVectorizer
vectorizer= CountVectorizer(analyzer="word", min_df = 2)
X=vectorizer.fit_transform(train["review"])
X=X.toarray()
y=train["sentiment"]

#Multinomial Naive Bayes
from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB()
clf.fit(X,y)
s=pickle.dumps(clf)
with open('model.p', 'wb') as f:
 f.write(s)

#Cross Validation
from sklearn import cross_validation 
cv= cross_validation.StratifiedKFold(y, n_folds=10)

scores=cross_validation.cross_val_score(clf, X, y, cv=cv)
print (scores)
print (np.mean(scores)) 

