import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data

class data_process:
    def __init__(self):
        print("Processing data")
        self.df = pd.read_csv('BlackFriday.csv')
        self.df.describe()
        # Do processing here
        
        
        