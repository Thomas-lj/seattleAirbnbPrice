import time
import datetime
import pandas as pd

def prepare_data(df, vars, cat_cols):
    """
    input
    df: DataFrame (input data)
    vars: list (numerical columns)
    cat_cols: list (categorical columns)

    Returns: filtered DataFrame with one-hot categorical encodings.
    """
    cols = vars  + cat_cols
    X = df.loc[:, df.columns.isin(cols)].copy()

    X = X.dropna(axis=0, subset=vars)
    # make date feature representing number of days as a host.
    if 'host_since' in cols:
        X['days_as_host'] = X.host_since.astype(str).apply(lambda x: time.mktime(datetime.datetime.strptime(x, "%m/%d/%Y").timetuple()))
        X = X.drop('host_since', axis=1)

    # Compute cat cols as new columns for each variable.
    for col in cat_cols:
        try:
            # for each cat add dummy var, drop original column, and compute dummy variables.
            X = pd.concat([X.drop(col, axis=1), pd.get_dummies(X[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=True)], axis=1)
        except:
            continue
    return X

if __name__ == '__main__':
    pass
