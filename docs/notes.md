# Analysis Notes

These checks use the original dataset before filtering by release year, type, or duration.

## Missing Values

- **Check:** `netflix_df.isna().sum()`
- **Finding:** I found zero pandas-detected missing values across all columns.
- **Meaning:** This is a useful starting point, but it does not prove every value is correct.
- **Learning:** `len(netflix_df['duration'].isna())` counts all rows because `.isna()` produces one Boolean value per row. Using `.sum()` counts the `True` values instead.

## Duplicate Records

- **Checks:** `netflix_df.duplicated().sum()` and `netflix_df['show_id'].duplicated().sum()`
- **Finding:** I found zero duplicate rows and zero repeated show IDs.
- **Meaning:** These checks found no repeated full records or identifiers. Repeated countries and directors are expected and are not duplicate records by themselves.

## Empty Text Values

- **Check:** Compare `director`, `cast`, and `country` with `''`, then count the matches using `.sum()`.
- **Finding:** Each column returned zero exact empty strings.
- **Limitation:** This check does not detect strings containing only spaces or placeholders such as `Unknown`.

## Next Questions

- Are there whitespace-only values or placeholders in the text columns?
- Do the column types match what the values represent?
- Would a missing director prevent me from analyzing movie duration? Why?

## Visualization Observations

To complete after reviewing the histogram:

- Most movies in this filtered dataset have durations between ___ and ___ minutes.
- Movies below ___ minutes appear less/more frequently than movies near 90 minutes.
