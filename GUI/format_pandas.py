import pandas as pd
import re as re
import numpy as np
import openpyxl

df = pd.read_excel('/Users/admin/Desktop/UNIL-Advanced-Programming-Project-2022/GUI/database.xlsx',
                   sheet_name='Sheet1', engine="openpyxl",index_col=0)

'''

def find_number(text):
    num = re.findall(r'[0-9]+',text)
    return " ".join(num)
df['Numbers']=df['Address'].apply(lambda x: find_number(x))

print(df.columns)

df['Zip_Code'] = df['Numbers'].str[-4:]


df['Zip_Code'] = df['Zip_Code'].replace({'0 21': '1000', '0 25': '1000', '0 26':'1000'})
df['Zip_Code'] = df['Zip_Code'].astype('float')
'''

dataset = df.iloc[: , :-28]
dataset = dataset.drop(['property_codes','address','available_from', 'prim_school',
              'floor','closest_shop','highway','kindergarten','public_transp','secon_school'], axis=1)

dataset.to_excel("/Users/admin/Desktop/UNIL-Advanced-Programming-Project-2022/GUI/dataset.xlsx")