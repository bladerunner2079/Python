import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import(ExponentialSmoothing,
                                        SimpleExpSmoothing,
                                        Holt)

df = yf.download("GOOG",  # Create dataframe and aggregate monthly frequency
                 start="2017-01-01",end="2020-08-12",
                 adjusted=True,
                 progress=False)

goog = df.resample("M") \
    .last() \
    .rename(columns={"Adj Close": "adj_close"}) \
    .adj_close


# print(df.head(100))


train_indices = goog.index.year < 2018  # Split test and training data
goog_train = goog[train_indices]
goog_test = goog[train_indices]

test_lenght = len(goog_test)  # Test control #1

# plt.plot(df)  # Plot stage 1 # Plotting dataframe
# plt.ylabel("goog")
# plt.show()

# Fitting SES models and create forecasting
ses_1 = SimpleExpSmoothing(goog_train).fit(smoothing_level=0.2)
ses_forecast_1 = ses_1(test_lenght)

ses_2 = SimpleExpSmoothing(goog_train).fit(smoothing_level=0.5)
ses_forecast_2 = ses_2(test_lenght)

ses_3 = SimpleExpSmoothing(goog_train).fit()
alpha = ses_3.model.params["smpothing_level"]
ses_forecast_3 = ses_3.forecast(test_lenght)


p



