# Netflix Content Analytics

![Histogram of movie durations under 90 minutes for titles released in 1990 or later](docs/images/short-movie-duration-histogram.png)

**First analysis: short-movie durations.** This histogram groups movies in the dataset released in 1990 or later with a runtime under 90 minutes into 10 duration intervals. Each bar shows the number of movies in that interval. The chart represents this filtered dataset, not Netflix's entire catalog.

An end-to-end data analytics project exploring trends in Netflix's content catalog. The project is being built incrementally to demonstrate the full analytics workflow: loading raw data, assessing data quality, cleaning and transforming records, exploring patterns, and communicating findings through visualizations.

![Line chart showing the number of movies in this dataset by release year](docs/images/movies-by-release-year.png)

Second analysis: movies by release year. This line chart counts movies in the dataset for each release year, including all durations. It shows how release years are represented in this dataset; it does not measure Netflix production, audience popularity, or when titles were added to Netflix.

> Project status: Work in progress. The current script checks missing values, duplicate rows, repeated show IDs, and empty text values. It also visualizes short-movie durations and movie counts by release year. Cleaning, reusable transformations, and additional analyses are planned next.

## Project Goal

The goal is to turn raw Netflix catalog data into a reproducible analysis that answers practical questions about the platform's content, including:

- How has the number of movies and TV shows changed over time?
- Which countries contribute the most titles?
- What genres appear most frequently in the catalog?
- How do movie durations vary by release year, country, or genre?
- When are titles typically added to Netflix?
- Are there noticeable gaps, duplicates, or inconsistencies in the data?

The first version uses a local CSV file. Later iterations will make the ingestion step reusable so similarly structured CSV files can be loaded, validated, and combined without rewriting the analysis.

## Planned Workflow

```text
Raw CSV files
    -> data validation
    -> cleaning
    -> transformation
    -> exploratory analysis
    -> visualizations
    -> documented insights
```

## Dataset

The analysis uses a local CSV at `datasets/netflix_data.csv` containing information about Netflix movies and TV shows. This file and the DataCamp starter notebook are not included in the repository because their redistribution terms have not been confirmed. To run the project, obtain your own copy of `netflix_data.csv` from the original DataCamp exercise and place it at that path.

| Column | Description |
| --- | --- |
| `show_id` | Unique identifier for a title |
| `type` | Movie or TV show |
| `title` | Title of the content |
| `director` | Director name or names |
| `cast` | Listed cast members |
| `country` | Country or countries associated with the title |
| `date_added` | Date the title was added to Netflix |
| `release_year` | Original release year |
| `duration` | Numeric duration; interpret in the context of `type` |
| `description` | Short content description |
| `genre` | Primary genre/category |

If the dataset is published later, its original source and redistribution terms should be confirmed and documented here. This project is for portfolio and educational purposes and is not affiliated with Netflix.

Movies and TV shows should be analyzed separately when interpreting `duration`; a movie's runtime and a show's number of seasons are different measures.

## Current Repository Structure

```text
project1/
|-- .gitignore
|-- docs/
|   `-- images/
|       |-- short-movie-duration-histogram.png
|       `-- movies-by-release-year.png
|-- h.py
`-- README.md
```

Create a local `datasets/` directory for the CSV before running the script. The structure will evolve as the project grows. Cleaning and transformation logic will eventually move into reusable modules, while generated charts and processed data will be kept separate from source data.

## Getting Started

Clone the repository and move into the project directory:

```bash
git clone https://github.com/YOUR_USERNAME/netflix-content-analytics.git
cd netflix-content-analytics
```

Create `datasets/` and put your own `netflix_data.csv` copy there before running the script.

On Windows PowerShell, create and activate a virtual environment, then install the current dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas numpy matplotlib jupyter
```

Run the initial analysis:

```powershell
python h.py
```

## Roadmap

- [x] Load the initial Netflix CSV with pandas
- [x] Perform a first filter of release year and duration
- [x] Visualize short-movie durations with a histogram and include a chart preview
- [x] Group movies by release year and visualize yearly counts with a line chart
- [ ] Profile missing values, duplicates, and inconsistent fields
- [ ] Build reusable loading and validation functions
- [ ] Clean dates, countries, genres, cast, and duration values
- [ ] Create analysis-ready transformed datasets
- [ ] Perform exploratory data analysis
- [ ] Build clear, accessible visualizations
- [ ] Summarize findings and limitations
- [ ] Add automated tests and dependency management

## Tools

- Python
- pandas and NumPy for data preparation
- Matplotlib for visualization
- Jupyter Notebook for exploration and documentation
- Git and GitHub for version control and project history

## Development Approach

This repository intentionally shows the project as it develops rather than presenting only a finished result. Each meaningful stage will be committed separately so that decisions, improvements, and lessons learned remain visible in the project history.

## Author

Created as a hands-on data analytics portfolio project.
My social accounts:   [LinkedIn](https://www.linkedin.com/in/john-miko-doinog-8a1769397/)