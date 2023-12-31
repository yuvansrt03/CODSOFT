# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JwpZewMAR81bfnQGwsWGt1yS3MWFhjKu
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv(r"movie_dataset.csv")

df.head()

def combine_features(row):
    return row['title']+' '+row['genres']+' '+row['director']+' '+row['keywords']+' '+row['cast']

features = ['genres', 'keywords', 'title', 'cast', 'director']

for feature in features:
    df[feature] = df[feature].fillna('')

df['combined_features'] = df.apply(combine_features, axis = 1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])

cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

movie_user_likes = "Spectre"
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
for i in sorted_similar_movies:
  print(get_title_from_index(i[0]));

