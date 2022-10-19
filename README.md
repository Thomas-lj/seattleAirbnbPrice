# Airbnb data analysis
##Section 1: Business Understanding
The purpose of this project is to analyze the Airbnb Seattle dataset
What should a guest on a tight budget consider when trying to book the next Airbnb accommodation for a night?
And as an Airbnb host, which area is considered a popular one when renting out your place?

This notebook seeks to investigate the following business quesions:
1) How do the prices differ from area to area in Airbnb listings?
2) Is there a cheapest time to go travel?
3) What is the most important contributor to a listing price?

## Data Understanding
This project uses 2 datasets collected in the time period 2016-2017:
- listings.csv: main metadata file for 3818 Airbnb listings.
- calendar.csv: 1048575 rows of detailed temporal data for the price and availability for each Airbnb.

## Data Preparation
From the listings.csv dataset, rows are removed if there is missing data in the following numerical columns:
- host_total_listings_count
- accommodates
- number_of_reviews
- review_scores_rating
- reviews_per_month
- host_since

After removing NaN entries, there are 3171 rows. NaN entries are removed using .dropna on the subset of numerical columns. This discards 647 rows and leaves a total of 3171 rows to model. The rows were removed instead of trying to impute values to avoid inducing model bias from missing data modelling. Note that future work could consider imputing values to save data, and then investigate how it affects the price predictions.

- host_response_time
- host_is_superhost
- neighbourhood_group_cleansed
- room_type
- bed_type
- instant_bookable
- cancellation_policy
- require_guest_phone_verification

## Question 1: How do the prices differ from area to area in Airbnb listings?
This plot shows the percentage of booked nights for each respective neighbourhood:
![Areas_percentage_of_booked_nights](https://user-images.githubusercontent.com/43189719/196300269-de35da4d-21e8-4ad5-8dcd-d9c61d293bd8.png)
With an average price of 140$/night the 89 Airbnbs in the area Cascase are booked 42% of the time.
With an average of 110$/night the 11 Airbnbs in the area Interbay are booked only 15% of the time.
The plot below shows the Airbnb price distributions for each Cleansed Are Group (sorted like the above plot with percentage occupancy).
![Area_prices_boxplot](https://user-images.githubusercontent.com/43189719/196302308-6f3e4f39-4f0b-4a1e-90e0-76c60275bced.png)


## Question 2: Is there a cheapest time to go travel?
The plot below shows the prices for available Airbnb listings averaged over weekdays and during the year. 
![prices_overview](https://user-images.githubusercontent.com/43189719/196335334-68a7501a-a34a-4787-8c9c-0202c2e3bd8a.png)

The prices are higher on average for the weekends, and the summer holiday months are the most expensive. The cheapest time to go is during winter/spring (especially around January).

## Question 3: What is the most important contributor to a listing price?
To identify features that are correlated with the Airbnb price, this shows a subset of the numerical features in this project:
![sns_heatmap](https://user-images.githubusercontent.com/43189719/196295209-117cab3d-fe35-464f-b485-ce9b6a856a11.png)

The resulting CV=5 averaged model Airbnb price predition is 0.55:
![scatter_plot_lin_model_price_prediction](https://user-images.githubusercontent.com/43189719/196295480-2955d00a-30f4-4043-bd3a-3d12179268d8.png)

The important averaged features for the linear model are
![feature_weights](https://user-images.githubusercontent.com/43189719/196295575-72a1166e-d575-48fc-a7b8-4358ff124512.png)
Among the most important features contributing positively to higher Airbnb prices are the areas Queen Anne, Cascade and Magnolia together with the feature accommodates (how many people the Airbnb accommodates).
The features contributing negatively to a price prediction are Shared room (if yes, the room could be shared with someone else) and the areas Northgate and Delridge.
The categorical NaN features (weight~0 in the above plot) contributes barely anything to the model performance. Future work can consider removing these features as they do not seem to change the model.

## Conclusion
- The Airbnbs areas in the Cascase and Capitol Hills have the highest fraction of booked Airbnb nights of all while Interbay and Northbay have the lowest.
- Airbnb prices are highest on Fridays and Saturdays. The cheapest season during the year is early in the year. If you want a cheaper trip, go during the weekdays in January.
- The Airbnb prices are most importantly determined by the neighbourhood, how many people it accommodates and whether the room is shared.


## Contributing Members
This work is contributed by the author, Thomas.

|Name     |  email   | 
|---------|-----------------|
|[Thomas git](https://github.com/[Thomas-lj])| thomasleichtjensen@gmail.com        |
Check out my [Medium blog post](https://medium.com/@thomasleichtjensen/seattle-airbnb-prices-overview-7d8a402bbe87) on this topic. Thanks for reading!
