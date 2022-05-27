import pandas as pd
import re as re
import numpy as np
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('GUI/gui_data/data.xlsx',
                   sheet_name='Sheet1', engine="openpyxl",index_col=0)

#Calcule price mean by zipcode
pricebyzip = df[['zip_code', 'price']].groupby(['zip_code'], as_index=False).mean()

pricebyrooms = df[['rooms', 'price']].groupby(['rooms'], as_index=False).mean()

pricebyzip.to_excel("GUI/gui_data/MeanPriceZIP.xlsx")

pricebyrooms.to_excel("GUI/gui_data/MeanPriceRooms.xlsx")