## Seattle Airbnb prices
### Objective
The purpose of this project is to  analyze the Airbnb Seattle dataset. The following project questions are investigated:
- Which neighbourhood is the most expensive?
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




## Contributing Members
This work is contributed by the author, Thomas.

|Name     |  email   | 
|---------|-----------------|
|[Thomas git](https://github.com/[Thomas-lj])| thomasleichtjensen@gmail.com        |

