# 🎬 Cinematic Alchemy: Ingredients for Movie Magic

You can find our datastory [here!](https://moviesuccess.github.io/)

## 📄 Abstract

This study aims to identify the key factors behind the success of a movie by examining how different success metrics vary based on several criteria.
Notably, we use two categories of success metrics: 

- **_Financial Metrics_** which include box-office revenue and profitability

- **_Popularity Metrics_** such as audience ratings and the tomatometer from RottenTomatoes - an aggregated measure of TV critics

Based on these metrics, we aim to understand how various characteristics of movies impact their success.
Specifically, we will explore the influence of the movie’s genre, release date timing, casting quality as well as movie length.
Through these analyses, we intend to establish the typical characteristics of movies that contribute to success for each category of metrics.

## ❓ Research Questions

- What is the impact of financial context on the success of a movie?
We want to assess how financial context, such as good economic periods or crisis affect the movie revenue. We want to observe if there is a correlation between a financial asset representing general economic health and yearly average of movie revenue. 
- How do the length of a movie and its release date contribute to its success?
- In what ways do trends in theme and genre influence the success of a movie?
- How does the fame and experience of actors and directors affect the success of a movie?

## 📊 Proposed Additional Datasets

### TMDB & Web Scraping 

TMDB website is a popular, user editable database for movies and TV shows. We use TMDB data from [**The Movies Dataset**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/) and the TMDB api to extract the box office revenue and the budget of missing values in our dataset

### CPI

We use the `cpi` Python library which allows us to compare monetary values adjusted for inflation.
The dataset itself used by `cpi` is the All Urban Consumers (CU) provided by The Bureau of Labor Statistics in the U.S. Department of Labor.

### S&P 500
We use S&P 500 data to compare financial context with movie revenue. The data are obtained with python library `yfinance`.

### RottenTomatoes

We deemed it crucial to compare audience scores from critics' scores. The RottenTomatoes website aggregates such movie ratings. The critics' score on RottenTomatoes is similar to that of Metacritic, but since RottenTomatoes also includes the audience score, we chose to use their [dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset/data) to have more consistent results. In our experience, the audience score and the critic's score are often very different, our exploratory data analysis reveals that there is only a 0.72 correlation between the two, which confirms our intuition that these metrics can be used for separate evaluations.

## 📈 Methods

### Measuring success

Instead of picking a single success metric, we perform our analyses using a selected set of metrics, as each of these metrics reveal a different aspect of a movie's success. Certain factors only influence a specific success metric, such as the release month only influencing revenue as opposed to ratings, as shown in the pipeline. Here are the various success metrics we considered:
- Audience score: measures popularity on a long term
- Critic score: measures the reception from movie critics
- Box Office Revenue: (10600 movies with box office revenue)
- Gross profit: measures the financial success (5600 movies with budget, so this metric reduces movie samples too much)
- Multiplicative Factor: measures the popularity on a short term by the factor between total revenue and first week revenue (not enough movies with both first week and total revenue)

### Genre clustering

Given that a movie can be assigned multiple genres, it is not satisfactory to analyze movies that have the exact same set of genres, because movies with rare intersection of genres wouldn't account for a statistically meaningful subset of all the movies. Therefore, we propose to cluster movies according to their genres.
One natural choice as a distance function is the Jaccard distance, as the value we want to cluster on is a set. A possible algorithm for clustering movies according to their genres would be the K-means clustering algorithm.

### Correlation

We use correlation to compare time-series of two variables and observe how they are related.

### Regression

We use regression to compare variables present across many movies, such as length, and success defined according to our variables. We will use R2 coefficients and visualization of the regression to assess the quality of our predictors. Furthermore, we will use t-test to observe if the relation obtained is statistically significant. 

### Actor success score

We build a metric for movies that reflects the overall quality and fame of casted actors. This will be computed by summing the number of actors that have played in a successful movie prior to the release date of the interested artwork. It will be used as an additional predictor in the regression.

## 🤝 Team Workload

| Individual Tasks	                 	| Team Member           |
|-----------------------------------------------|-----------------------|
| Pipeline                               	| Benjamin Krieger      |
| Financial Research Questions           	| Maxence Hofer         |
| Genre Research Questions               	| Joseph Fourment       |
| Length and Release Date Research Questions 	| Paul McIntyre      	|
| Actors Research Questions              	| Luc Guyot             |


## 🗓️ Proposed Timeline

| Date         | Milestone                                                					|
|--------------|------------------------------------------------------------------------------------------------|
| Nov 24       | Complete the data pipeline and begin answering research questions				|
| Dec 1        | Finish first MVP (Minimum Valuable Product) with basic analysis and data story structure	|
| Dec 8        | Continue answering research questions, improve data story visuals				|
| Dec 15       | Finish data story										|
| Dec 22       | Resolve any remaining issues and submit the final report					|

![image](https://github.com/epfl-ada/ada-2023-project-madafaka1/assets/47635960/64d93d4d-1144-460f-ae89-7af5c7f65046)
