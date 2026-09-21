import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = 'datasets/netflix_data.csv'
netflix_df = pd.read_csv(data)
#print(netflix_df.head())

#displaying only year 1990 and above
netflix_1990_and_above = netflix_df[netflix_df['release_year'] >= 1990]
#highest duration to low
netflix_frequent_duration = netflix_1990_and_above.sort_values('duration', ascending=False) 
#select only relevant columns       
netflix_selected_columns = netflix_frequent_duration[['title','country','release_year','duration']]

#count the short movies that are less than 90 mins
short_movies_count = netflix_selected_columns[netflix_selected_columns['duration']<90]
#print(netflix_selected_columns.head(10))
print(short_movies_count.head(20))
