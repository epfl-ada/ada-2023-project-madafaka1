import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def convert_and_extract_date(df):
    """
    Convert and extract date-related features from the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the 'Movie release date' and 'Movie runtime' columns.

    Returns:
    pd.DataFrame: Updated DataFrame with added 'Month' and 'Year' columns.

    Example:
    >>> df = convert_and_extract_date(input_df)
    """
    # Convert 'Movie release date' to datetime
    df['Movie release date'] = pd.to_datetime(df['Movie release date'])
    # Extract month and year from the release date
    df['Month'] = df['Movie release date'].dt.month
    df['Year'] = df['Movie release date'].dt.year
    return df

def create_length_bins(df, min_sample_size=25):
    """
    Create bins for movie length with a step of 15 minutes up to 300 minutes and aggregate data based on the bins.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with 'Movie runtime' column.
    - min_sample_size (int): Minimum sample size for valid bins.

    Returns:
    pd.DataFrame: Filtered DataFrame with added 'Length Bin' column.
    pd.DataFrame: Aggregated data based on the length bins.

    Example:
    >>> filtered_df, grouped_data = create_length_bins(input_df)
    """
    # Create bins for movie length 
    bins = list(range(0, 315, 15))
    # Assign movies to bins based on Movie Length
    df['Length Bin'] = pd.cut(df['Movie runtime'], bins=bins, right=False)
    # Filter out bins with a small sample size (adjust the threshold as needed)
    valid_bins = df['Length Bin'].value_counts()[df['Length Bin'].value_counts() >= min_sample_size].index
    filtered_movies = df[df['Length Bin'].isin(valid_bins)]
    # Group by the length bins and calculate the median of Box Office Revenue, Tomatometer Rating, and Audience Rating for each bin
    grouped_data = filtered_movies.groupby('Length Bin').agg({
        'Movie box office revenue': 'median',
        'tomatometer_rating': 'mean',
        'audience_rating': 'mean'
    }).reset_index()

    return filtered_movies, grouped_data

def plot_movie_duration_metrics(grouped_data):
    """
    Plot various movie duration metrics.

    Parameters:
    - grouped_data (pd.DataFrame): Aggregated data based on movie length bins.

    Example:
    >>> plot_movie_duration_metrics(aggregated_data)
    """
    plt.figure(figsize=(18, 6))
    # Plotting the median box office revenue per movie duration
    plt.subplot(1, 3, 1)
    sns.barplot(x='Length Bin', y='Movie box office revenue', data=grouped_data)
    plt.title('Median Box Office Revenue per Movie Duration')
    plt.xlabel('Movie Duration (minutes)')
    plt.ylabel('Median Box Office Revenue')
    plt.xticks(rotation=45)
    plt.xlim(2, 14)
    # Plotting tomatometer_rating per movie duration
    plt.subplot(1, 3, 2)
    sns.barplot(x='Length Bin', y='tomatometer_rating', data=grouped_data)
    plt.title('Mean Tomatometer Rating per Movie Duration')
    plt.xlabel('Movie Duration (minutes)')
    plt.ylabel('Mean Tomatometer Rating')
    plt.xticks(rotation=45)
    plt.xlim(2, 14)
    # Plotting audience_rating per movie duration
    plt.subplot(1, 3, 3)
    sns.barplot(x='Length Bin', y='audience_rating', data=grouped_data)
    plt.title('Mean Audience Rating per Movie Duration')
    plt.xlabel('Movie Duration (minutes)')
    plt.ylabel('Mean Audience Rating')
    plt.xticks(rotation=45)
    plt.xlim(2, 14)

    plt.tight_layout()
    plt.show()

def explore_month_release_relationship(df, month_order):
    """
    Explore the relationship between movie month release and various metrics.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with 'Month' column.
    - month_order (list): List of month names in the desired order.

    Example:
    >>> explore_month_release_relationship(input_df, ['Jan', 'Feb', ..., 'Dec'])
    """

    # Map the numeric month values to month names
    df['Month'] = list(map(lambda x: month_order[x - 1], df['Month']))

    plt.figure(figsize=(18, 6))
    # Plotting the relationship between movie month release and box office revenue
    plt.subplot(1, 3, 1)
    sns.boxplot(x='Month', y='Movie box office revenue', data=df, order=month_order)
    plt.title('Box Office Revenue by Release Month')
    plt.xlabel('Release Month')
    plt.ylabel('Box Office Revenue')
    plt.ylim(0, 2.7e8)
    # Plotting tomatometer_rating per movie duration
    plt.subplot(1, 3, 2)
    sns.boxplot(x='Month', y='tomatometer_rating', data=df)
    plt.title('Tomatometer Rating by Release Month')
    plt.xlabel('Release Month')
    plt.ylabel('Tomatometer Rating')
    # Plotting audience_rating per movie duration
    plt.subplot(1, 3, 3)
    sns.boxplot(x='Month', y='audience_rating', data=df)
    plt.title('Audience Rating by Release Month')
    plt.xlabel('Release Month')
    plt.ylabel('Audience Rating')

    plt.tight_layout()
    plt.show()
