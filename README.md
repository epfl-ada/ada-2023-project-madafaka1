# Recipe for a successful movie

## Abstract

We seek to identify what makes a movie successful by studying how different success metrics vary depending on a number of criteria.
Notably, we use as success metrics:: the box-office revenue, the difference between the budget and revenue, the audience rating, and the tomatometer from RottenTomatoes, which is an aggregated measure of TV critics. 

We seek to identify what makes a movie successful by studying how different success metrics vary depending on a number of criteria.
Notably, we use two categories of success metrics: 
financial metrics which are composed of box-office revenue and profitability
quality metrics such as the audience rating, and the tomatometer from RottenTomatoes, which is an aggregated measure of TV critics
	Based on those, we want to understand how characteristics of movies impact the different metrics. In particular, we will study the role of the movie’s type, the release timing, 

## Research Questions

- How financial context influences the success of a movie
- How the length of a movie and its release date affect its success 
- How trends in theme and genre can affect the success of a movie
- How actors’ and directors’ fame/experience affect the success of a movie

## Proposed Additional Datasets

### TMDB & Web Scraping 

We extract TMDB data from [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/) and the TMDB api to extract the box office revenue and the budget of missing values in our dataset

### CPI

We use the `cpi` Python library which allows us to compare monetary values adjusted for inflation.
The dataset itself used by `cpi` is the All Urban Consumers (CU) provided by The Bureau of Labor Statistics in the U.S. Department of Labor.

### S&P 500
We use S&P 500 data to compare financial context with movie revenue. The data are obtained with python library yfinance.

### RottenTomatoes

We deemed it crucial to compare audience scores from critics' scores. The RottenTomatoes website aggregates such movie ratings. The critics' score on RottenTomatoes is similar to that of Metacritic, but since RottenTomatoes also includes the audience score, we chose to use their dataset to have more consistent results. In our experience, the audience score and the critic's score are often very different, our exploratory data analysis reveals that there is only a TODO: XXX correlation between the two, which confirms our intuition.

## Methods

### Measuring success

Instead of picking a single success metric, we perform our analyses using a selected set of metrics, as each of these metrics reveal a different aspect of a movie's success. Certain factors only influence a specific success metric, such as the release month only influencing revenue as opposed to ratings, as shown in the pipeline. Here are the various success metrics we considered:
- Audience score: measures popularity on a long term
- Critic score: measures the reception from movie critics
- Box Office Revenue: (10600 movies with revenue)
- Gross profit: measures the financial success (5600 movies with budget, so this metric reduces movie samples too much)
- Multiple: measures the popularity on a short term by the factor between total revenue and first week revenue (not enough movies with total revenue)

### Genre clustering

Given that a movie can be assigned multiple genres, it is not satisfactory to analyze movies that have the exact same set of genres, because movies with rare intersection of genres wouldn't account for a statistically meaningful subset of all the movies. Therefore, we propose to cluster movies according to their genres.
One natural choice as a distance function is the Jaccard distance, as the value we want to cluster on is a set. A possible algorithm for clustering movies according to their genres would be the K-means clustering algorithm.

### Correlation

We use correlation to compare time-series of two variables and observe how they are related.

### Regression

We use regression to compare variables present across many movies, such as length, and success defined according to our variables. We will use R^2 coefficients and visualization of the regression to assess quality of our predictors.

## Proposed timeline

- 24 November: Complete the data pipeline and begin to answer research questions
- 1 December: Finish MVP (Minimum Valuable Product) with few analysis but the data story structure
- 8 December: Continue answering research question, improve data story visual
- 15 December: Finish data story
- 22 December: solve last issues and submit report 
