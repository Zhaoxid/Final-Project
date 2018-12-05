import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data

class data_process:
    def __init__(self):
        print("Processing data")
        self.df = pd.read_csv('BlackFriday.csv')
        self.df.describe()
        self.df.shape
        # Do processing here
        self.df = self.df.fillna(0) # replace NA with 0, no purchase from that catagory 
        
        self.df['Gender'] = self.df['Gender'].apply(self.map_gender)
        self.df['Age'] = self.df['Age'].apply(self.map_age)
        self.df['City_Category'] = self.df['City_Category'].apply(self.map_city_categories)
        self.df['Stay_In_Current_City_Years'] = self.df['Stay_In_Current_City_Years'].apply(self.map_stay)    
        
        cols = ['User_ID','Product_ID']
        self.df.drop(cols, inplace = True, axis =1)


    def map_gender(self, gender):
        if gender == 'M':
            return 1
        else:
            return 0
        
    def map_age(self, age):
        if age == '0-17':
            return 0
        elif age == '18-25':
            return 1
        elif age == '26-35':
            return 2
        elif age == '36-45':
            return 3
        elif age == '46-50':
            return 4
        elif age == '51-55':
            return 5
        else:
            return 6

    def map_city_categories(self, city_category):
        if city_category == 'A':
            return 2
        elif city_category == 'B':
            return 1
        else:
            return 0

    def map_stay(self, stay):
        if stay == '4+':
            return 4
        else:
            return int(stay)
