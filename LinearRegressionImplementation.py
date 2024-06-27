############# Straight Line y = m(x) + c
############# Where : y = dependent variable, x = in-dependent variable, m = slope , c = intercept
############# Calculating The Mean
import pandas as pd

def mean(data):
    mean_X = 0
    mean_Y = 0
    counter = 0
    for values in data.iloc[:,1]:
        mean_X = mean_X + values
        counter+=1
    for values in data.iloc[:,0]:
        mean_Y = mean_Y + values
    mean_X = mean_X /counter
    mean_Y = mean_Y /counter
    return [mean_X,mean_Y]

############# Calculating the slope and intercept
def get_slope_intercept(data):
    data['x-mean'] = data.iloc[:,1] - mean(data)[0]
    data['y-mean'] = data.iloc[:,0] - mean(data)[1]
    data['x-mean-square'] = data['x-mean']*data['x-mean']
    data['x-mean-*-y-mean'] = data['x-mean']*data['y-mean']
    sum_slope_numerator = 0
    sum_x_mean_square = 0
    for values in data['x-mean-square']:
        sum_x_mean_square = sum_x_mean_square + values
    for values in data['x-mean-*-y-mean']:
        sum_slope_numerator = sum_slope_numerator + values
    slope = sum_slope_numerator / sum_x_mean_square
    ###########intercept = c
    intercept = mean(data)[1] - (slope*mean(data)[0])
    return [slope,intercept]

############# Predicting new values
def predict(Data):
    lenght=len(Data.index)
    Max = max(Data.Time)
    X = list(Data.Time)
    Y = list(Data.Price)
    Index = list(Data.index)
    next_3_values = [int(x) for x in range(int(Max+1),int(Max+4))]
    slope = get_slope_intercept(Data)[0]
    intercept =  get_slope_intercept(Data)[1]
    for time in next_3_values:
        new_value = (slope*time) + intercept
        last_date = Index[-1]
        if int(last_date.split('-')[1]) == 12:
            new_date = str(int(last_date.split('-')[0])+1)+'-'+ '1'
        elif int(last_date.split('-')[1]) < 12:
            new_date = str(last_date.split('-')[0])+'-'+str(int(last_date.split('-')[1])+1)
        X.append(time)
        Y.append(new_value)
        Index.append(new_date)
    new_data = pd.DataFrame({'Time':X,'Price':Y,'Date':Index})
    new_data = new_data.set_index('Date')
    return new_data
