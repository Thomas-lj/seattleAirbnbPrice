import seaborn as sns
import pandas as pd
import os
import matplotlib.pyplot as plt
df = pd.read_csv(os.path.abspath("../data/listings.csv"))

# remove $ , and .00 from price col. cast to int.
df['price'] = df.price.astype(str).apply(lambda x: x.replace('$', '').replace('.00', '').replace(',', '')).astype(int)
# host_response_rate num 0-100 %, remove %
df['host_response_rate'] = df.host_response_rate.astype(str).apply(lambda x: x.replace('%', ''))

date_cols = [
    'host_since',
]

vars = [
    'price',
    'host_total_listings_count', # ok
    'latitude', # ok
    'longitude', # ok
    'accommodates', # ok
    'guests_included', # ok
    'number_of_reviews', # ok
    'review_scores_rating', # ok
    'reviews_per_month' # ok
]

# 'host_response_rate', # turn into categorigal value?



cat_col = [
    'host_response_time',
    'host_is_superhost',
    'host_neighbourhood',
]   

corr = df[vars].corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)
