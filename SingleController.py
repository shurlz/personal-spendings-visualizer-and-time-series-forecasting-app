import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from LinearRegressionImplementation import predict
from PIL import Image

data = pd.read_csv('shurlz_database.csv')#,parse_dates=['Date'],index_col='Date')
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['yr_mt'] = data['Year'].astype('str')+'-'+data['Month'].astype('str')
date_ = pd.DataFrame(data.groupby('yr_mt').sum()['Price'])
date_['Time'] = np.arange(len(date_.index))
date_['Rolling_mean'] = date_['Price'].rolling(window=2).mean()

def data_predict():
    data = predict(date_)
    return data

def time_series():
    x = date_[:].index
    y = date_[:].Price
    plt.plot(x, y,'*--', color='gray')
    plt.title('Amount spent monthly')
    plt.savefig('E_prediction.png', bbox_inches='tight', dpi=100)
    image = Image.open('E_prediction.png')
    image = image.resize((591, 361), resample=Image.LANCZOS)
    image.save('E_prediction.png')

print(time_series())