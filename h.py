import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset.

data_path = 'datasets/netflix_data.csv'
netflix_df = pd.read_csv(data_path)

# Check the original dataset before filtering.

print(f'Total rows: {len(netflix_df)}')
print('\nMissing values by column:')
print(netflix_df.isna().sum())

print(f'\nDuplicate rows: {netflix_df.duplicated().sum()}')
print(f"Duplicate show IDs: {netflix_df['show_id'].duplicated().sum()}")

print(f"\nEmpty director values: {(netflix_df['director'] == '').sum()}")
print(f"Empty cast values: {(netflix_df['cast'] == '').sum()}")
print(f"Empty country values: {(netflix_df['country'] == '').sum()}")

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

print(f'\nShort movies released in 1990 or later: {short_movies_count}')

# Plot the distribution of short-movie durations.

plt.hist(
    short_movies['duration'],
    bins=10,
    edgecolor='black'
)
plt.title('NETFLIX SHORT-MOVIES RELEASED IN 1990 OR LATER')
plt.xlabel('duration (in minutes)')
plt.ylabel('number of movies')
plt.tight_layout()
plt.show()
plt.clf()

# Most movies in this filtered dataset have durations between ___ and ___ minutes.
# Movies below ___ minutes appear less/more frequently than movies near 90 minutes.

movies_duration = ['type', 'duration', 'release_year']
netflix_movies_duration = netflix_df[movies_duration]
netflix_movies_duration = netflix_movies_duration[netflix_movies_duration['type'] == 'Movie']
# print(netflix_movies_duration.head(10))

count_per_year = (
    netflix_movies_duration.groupby('release_year')
    .size()
    .reset_index(name='movie_count')
)

plt.plot(
    count_per_year['release_year'],
    count_per_year['movie_count']
)
plt.xlabel('release year')
plt.ylabel('number of movies')
plt.title('NETFLIX MOVIES BY RELEASE YEAR')
plt.tight_layout()
plt.show()
plt.clf()

# Country analysis: which countries contribute the most titles.

# Many titles have missing or empty country values.
# Keep only rows where country is actually recorded.
titles_with_country = netflix_df[
    netflix_df['country'].notna()
    & (netflix_df['country'] != '')
]

print(f'\nTitles with a recorded country: {len(titles_with_country)}')

# Count the top 10 country values by number of titles.
# Note: the country column can hold several countries per title
# (e.g. "United States, India"), so this counts the combined text.
country_counts = titles_with_country['country'].value_counts().head(10)
print('\nTop 10 countries by number of titles:')
print(country_counts)

# Horizontal bar chart because country names are long.
plt.barh(
    country_counts.index,
    country_counts.values,
    color='mediumseagreen',
    edgecolor='black'
)
plt.title('TOP 10 COUNTRIES BY NUMBER OF NETFLIX TITLES')
plt.xlabel('number of titles')
plt.ylabel('country')
plt.gca().invert_yaxis()  # highest count at the top
plt.tight_layout()
plt.show()
plt.clf()

# TV show analysis: distribution of seasons across shows.

# The duration column holds seasons for TV shows and minutes for movies.
# Analyzing them separately follows the note in the README.
netflix_tv_shows = netflix_df[netflix_df['type'] == 'TV Show']

print(f'\nTotal TV shows in the dataset: {len(netflix_tv_shows)}')

# Count how many shows have each season count.
# sort_index() keeps the x-axis in numeric order (1, 2, 3, ...).
season_counts = netflix_tv_shows['duration'].value_counts().sort_index()
print('\nNumber of shows by season count:')
print(season_counts)

# Vertical bar chart: seasons on the x-axis, number of shows on the y-axis.
plt.bar(
    season_counts.index,
    season_counts.values,
    color='steelblue',
    edgecolor='black'
)
plt.title('NETFLIX TV SHOWS BY NUMBER OF SEASONS')
plt.xlabel('number of seasons')
plt.ylabel('number of shows')
plt.tight_layout()
plt.show()
plt.clf()
