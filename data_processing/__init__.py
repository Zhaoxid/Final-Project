import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns
import matplotlib as mlp

class data_process:
    def __init__(self):
        print("Processing data")
        self.df = pd.read_csv('BlackFriday.csv')
        self.df.describe()
        self.df.shape
        # Do processing here
        self.df = self.df.fillna(0) # replace NA with 0, no purchase from that catagory 
        
        sns.countplot(self.df['Age'],hue=self.df['Gender'])
        explode = (0.1,0)  
        fig1, ax1 = plt.subplots(figsize=(12,7))
        ax1.pie(self.df['Gender'].value_counts(), explode=explode,
                labels=['Male','Female'], autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')  
        plt.tight_layout()
        plt.legend()
        
        explode = (0.1, 0, 0)
        fig1, ax1 = plt.subplots(figsize=(12,7))
        ax1.pie(self.df['City_Category'].value_counts(),explode=explode, 
                labels=self.df['City_Category'].unique(), autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')  
        plt.tight_layout()
        plt.legend()
        
        explode = (0.1, 0)
        fig1, ax1 = plt.subplots(figsize=(12,7))
        ax1.pie(self.df['Marital_Status'].value_counts(),explode=explode, labels=['Married','Not Married'], autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')  
        plt.tight_layout()
        plt.legend()


        fig1, ax1 = plt.subplots(figsize=(12,7))
        self.df['Occupation'].value_counts().sort_values().plot('bar')
        
        plt.show()

#         self.df['combined_G_M'] = self.df.apply(lambda x:'%s - %s' % (x['Gender'],x['Marital_Status']),axis=1)
#         sns.countplot(self.df['Age'],hue=self.df['combined_G_M'])
#         sns.countplot(self.df['Purchase'],hue=self.df['Occupation'])
#         plt.show()
        
        self.df['Gender'] = self.df['Gender'].apply(self.map_gender)
        self.df['Age'] = self.df['Age'].apply(self.map_age)
        self.df['Occupation'] = self.df['Occupation'].apply(self.map_occupation)
        self.df['City_Category'] = self.df['City_Category'].apply(self.map_city_categories)
        self.df['Stay_In_Current_City_Years'] = self.df['Stay_In_Current_City_Years'].apply(self.map_stay) 
        self.df['Purchase'] = self.df['Purchase'].apply(self.map_purchase)
        
        cols = ['User_ID','Product_ID']
        self.df.drop(cols, inplace = True, axis =1)

    def map_occupation(self, occupation):
        if ((occupation == 8) or (occupation == 9) or 
        (occupation == 18) or (occupation == 13) or 
        (occupation == 19) or (occupation == 11) or
        (occupation == 15) or (occupation ==  5) or
        (occupation == 10)):
            return 1
        elif ((occupation == 3) or (occupation == 6) or
        (occupation == 16) or (occupation == 2) or
        (occupation == 14) or (occupation == 12)):
            return 1
        else:
            return 0
    
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
      
    def map_purchase(self, purchase):
        if purchase <= 8000:
            return 1
        elif purchase > 8000 and purchase <= 10000:
            return 2
        elif purchase > 10000 and purchase <= 18000:
            return 3
        elif purchase > 18000 and purchase <= 20000:
            return 4
        else:
            return 5
