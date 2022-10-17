## Seattle Airbnb prices
### Objective
The purpose of this project is to  analyze the Airbnb Seattle dataset. The following project questions are investigated:
- Which neighbourhood is the hottest?
- What is the cheapest time to go travel?
- What features contribute to a higher/lower rental price?

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](data folder) within this repo.
3. Data processing/transformation script is being kept [here](scripts folder)
4. Execute the main.ipynb Jupyter Notebook for data analysis and plots.

## Data Description
This project uses 2 datasets collected in the time period 2016-2017:
- listings.csv: main metadata file for 3818 Airbnb listings.
- calendar.csv: 1048575 rows of detailed temporal data for the price and availability for each Airbnb.

## Data processing
From the listings.csv dataset, rows are removed if there is missing data in the following numerical columns:
- host_total_listings_count
- accommodates
- number_of_reviews
- review_scores_rating
- reviews_per_month
- host_since

After removing NaN entries, there are 3171 rows.
- host_response_time
- host_is_superhost
- neighbourhood_group_cleansed
- room_type
- bed_type
- instant_bookable
- cancellation_policy
- require_guest_phone_verification

## Neighbourhood popularity
This plot shows the percentage of booked nights for each respective neighbourhood:
![Areas_percentage_of_booked_nights](https://user-images.githubusercontent.com/43189719/196300269-de35da4d-21e8-4ad5-8dcd-d9c61d293bd8.png)
With an average price of 140$/night the 89 Airbnbs in the area Cascase are booked 42% of the time.
With an average of 110$/night the 11 Airbnbs in the area Interbay are booked only 15% of the time.

## Time variations
The plot below shows the prices for available Airbnb listings averaged over weekdays and during the year. 
![prices_overview](https://user-images.githubusercontent.com/43189719/196295782-064afa23-1aaa-41b7-a566-7f4c80ab2b45.png)
The prices are higher on average for the weekends, and the summer holiday months are the most expensive. The cheapest season is during the spring.

## Linear Modelling
To identify features that are correlated with the Airbnb price, this shows a subset of the numerical features in this project:
![sns_heatmap](https://user-images.githubusercontent.com/43189719/196295209-117cab3d-fe35-464f-b485-ce9b6a856a11.png)

The resulting CV=5 averaged model Airbnb price predition is 0.55:
![scatter_plot_lin_model_price_prediction](https://user-images.githubusercontent.com/43189719/196295480-2955d00a-30f4-4043-bd3a-3d12179268d8.png)

The important averaged features for the linear model are
![feature_weights](https://user-images.githubusercontent.com/43189719/196295575-72a1166e-d575-48fc-a7b8-4358ff124512.png)
, note that the categorical NaN features (weight~0) contributes barely anything to the model performance. Future work can consider removing these features as they do not seem to change the model.

## Linear Modelling
- The Airbnbs in the South Lake Union has the highest fraction of booked Airbnb nights of all. 


## Contributing Members
This work is contributed by the author, Thomas.

|Name     |  email   | 
|---------|-----------------|
|[Thomas git](https://github.com/[Thomas-lj])| thomasleichtjensen@gmail.com        |

