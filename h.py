import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset.
data_path = 'datasets/netflix_data.csv'
netflix_df = pd.read_csv(data_path)

# Keep titles released in 1990 or later.
netflix_1990_and_above = netflix_df[netflix_df['release_year'] >= 1990]

# Keep movies with a duration under 90 minutes.
short_movies = netflix_1990_and_above[
    (netflix_1990_and_above['type'] == 'Movie')
    & (netflix_1990_and_above['duration'] < 90)
]

selected_columns = ['title', 'type', 'country', 'release_year', 'duration']
short_movies = short_movies[selected_columns]
short_movies = short_movies.sort_values('duration', ascending=False)
short_movies_count = len(short_movies)

print(short_movies.head(20))
print(f'short movies released in 1990 or later: {short_movies_count}')
