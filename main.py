import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Business questions:
# 1) How can we predicts an airbnb price?
# 2) When is the best time to visit?
# 3) How do you get a good review rating?

df = pd.read_csv(os.path.abspath("./data/listings.csv"))

var_cols = [
    'host_listings_count', # NA=0?
    'host_total_listings_count', # NA=0?
    'latitude',
    'longitude',
    'accomodates',
    'bathrooms',
    'bedrooms',
    'beds',
    'square_feet',
    'guests_included',
    'minimum_nights', 'maximum_nights', 'availability_30',
       'availability_60', 'availability_90', 'availability_365',
       'number_of_reviews', 'review_scores_rating', 'review_scores_accuracy',
       'review_scores_cleanliness', 'review_scores_checkin',
       'review_scores_communication', 'review_scores_location',
       'review_scores_value', 'license', 'calculated_host_listings_count',
       'reviews_per_month'
]
cat_df = df.select_dtypes(include=['object'])
y = df.price
X = df[:, df.columns != 'price']
cat_dummies = cat_df.get_dummies(cat_df)   # Use this cell to write whatever code you need.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

lin_model = LinearRegression(X_train, y_train)