import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from PIL import Image

def users_database():
    files = os.listdir()
    if 'shurlz_database.csv' in files:
        pass
    else:
        users_database = pd.DataFrame(columns=['Name', 'Price', 'Date'])
        users_database.to_csv('shurlz_database.csv', index=False)
    if 'personal_info.csv' in files:
        pass
    else:
        users_info = pd.DataFrame({'Budget': 0} ,index=[0])
        users_info.to_csv('user_info_database.csv', index=False)

def add_new_spending(Name=None,Price=None,Date=None):
    if type(Name) == str and type(Price) == int:
        data = pd.read_csv('shurlz_database.csv')
        new_data=  {'Name':Name, 'Price': Price ,'Date': Date}
        shurlz = data.append(new_data,ignore_index=True)
        os.remove('shurlz_database.csv')
        shurlz.to_csv('shurlz_database.csv', index=False)
        return True

data = pd.read_csv('shurlz_database.csv')

data['Date'] = pd.to_datetime(data.Date)
data['Year'] = pd.to_datetime(data.Date).dt.year
data['Month'] = pd.to_datetime(data.Date).dt.month
data['Day'] = pd.to_datetime(data.Date).dt.day
default_end = str(data['Date'].max()).split(" ")[0].split("-")
default_start = str(data['Date'].min()).split(" ")[0].split("-")
default_max_price = data['Price'].sum()
default_min_price = 0

def Return(default,user):
    string = 'string'
    integer = 1011
    try:
        if type(user) == type(string) or type(integer):
            user = int(user)
            return user
        else:
            return default
    except:
        return default

def plot_products(): ### General product plotting
    data.groupby('Name').sum()['Price'].plot(kind='bar')
    plt.savefig('C_products_by_price.png',bbox_inches='tight',dpi=100)
    time.sleep(4)

def plot_by_year_month_day(s_user_yr=None,s_user_mt=None,s_user_day=None,e_user_yr=None,e_user_mt=None,e_user_day=None,
                          u_min_price=None,u_max_price=None):
    new_data_frame = pd.DataFrame(data.groupby(['Year', 'Month', 'Day']).sum()['Price'])
    new_data_frame_without_day = pd.DataFrame(data.groupby(['Year', 'Month']).sum()['Price'])
    start_year = Return(int(default_start[0]),s_user_yr)
    start_month = Return(int(default_start[1]),s_user_mt)
    start_day = Return(int(default_start[2]),s_user_day)
    end_year = Return(int(default_end[0]),e_user_yr)
    end_month = Return(int(default_end[1]),e_user_mt)
    end_day = Return(int(default_end[2]),e_user_day)
    max_price = Return(default_max_price,u_max_price)
    min_price = Return(default_min_price,u_min_price)
    stage_1_data = new_data_frame.loc[(start_year, start_month, start_day):(end_year, end_month, end_day)]
    price_recorgnized_1 = stage_1_data[(stage_1_data['Price']>=min_price)&(stage_1_data['Price']<=max_price)]
    price_recorgnized_1.plot(kind='barh')
    plt.savefig('A_year_month_day.png', bbox_inches='tight', dpi=100)
    # without the day.............................................................................................
    stage_2_data_without_day = new_data_frame_without_day.loc[(start_year, start_month):(end_year, end_month)]
    price_recorgnized_2_without_day = stage_2_data_without_day[(stage_2_data_without_day['Price']>=min_price)&(stage_2_data_without_day['Price']<=max_price)]
    price_recorgnized_2_without_day.plot(kind='barh')
    plt.savefig('B_year_month.png', bbox_inches='tight', dpi=100)
    # plotting others
    plot_most_spent_on_item()
    plot_products()
    time.sleep(3)
    plot_resize()

def plot_most_spent_on_item():
    data.Name.value_counts().plot(kind='bar')
    plt.savefig('D_most_spent_on_item.png',bbox_inches='tight',dpi=100)

def plot_resize():
    for files in os.listdir():
        if files.split('.')[-1] == 'png':
            name = files.split('.')[0]
            image = Image.open(files)
            if int(image.width)!=591 and int(image.height)!=361:
                image = image.resize((591,361),resample=Image.LANCZOS)
                image.save(f'{name}.png')

def all_plots():
    plots = []
    for files in os.listdir():
        if files.split('.')[-1] == 'png':
            plots.append(files)
    return plots

class allplots:
    def __init__(self,count):
        self.count = -1
        self.plots = all_plots()
    def change_plot(self):
        if self.count < len(self.plots)-1:
            self.count+=1
        return self.plots[self.count]

#print(show_all_plots())
print(plot_by_year_month_day())
#print(all_plots())
#plots = allplots('plots')
#print(plots.change_plot())
