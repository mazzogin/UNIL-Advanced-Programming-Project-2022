import pandas as pd


# To do
# Reorder Data
# Put Dummy variables into 0/1 format
# Put dummy varibales into long format
# Remove N/A's by replacing to the mean of the category by zip_code or by replacing by 0
# Say which columns contain which kind of value
# Extract ZIP codes (write small function that always extracts four consecutive number values)

# What to do about the floors? Some indicate how many floors a house has, some indicate in which floor the apartment is located.
# Furthermore there is to decide what to do with N/A's and EG (Ground Floor).
# What do we fill the N/A's with and how do we declare which floor the ground floor is on (logically it would  be 0 obviously, 
# but then what do we put into the N/A's)?

property_codes = pd.read_csv(r'data/property_codes.csv')
property_details = pd.read_csv(r'data/property_details.csv')


database = pd.concat([property_codes, property_details], axis=1)

database = database[[
    'Property_Codes', 'address', 'price','rooms', 'sq_meters', 'available_from', 'contruction_year', 
    'type', 'floors', 'balcony', 'dishwasher', 'elevator', 'closest_shop', 'highway','kindergarten',	
    'parking_ext', 'parking_int', 'prim_school', 'public_transp', 'secon_school', 'dryer',	
    'wash_m','tv','url']]

database.rename(columns={'Property_Codes':'property_codes',
                         'type':'property_type',
                         'contruction_year':'construction_year',
                         'floors':'floor'
                         }, inplace = True)

### Adding Columns

# Create a new column containing the ZIP code location
database['zip_code'] = database['address'].str.extract('(\d{4})').astype(int)

### Basic Cleaning and setting of data types (also removing commas, unwanted strings etc.)

## 'property_codes'
database['property_codes'] = database['property_codes'].replace(',', '')

## 'price'
# Delete unwanted strings in column 'price'
database['price'] = database['price'].str.replace(',','')
database['price'] = database['price'].str.replace('sur demande', '0')
database['price'] = database['price'].str.replace("'", '')
database['price'] = pd.to_numeric(database['price'], errors='coerce')
database['price'] = database['price'].fillna(0)

## 'rooms'
database['rooms'] = database['rooms'].replace('Non disponible', '0')
database['rooms'] = pd.to_numeric(database['rooms'], errors='coerce')

## 'sq_meters'
database['sq_meters'] = database['sq_meters'].replace('Non disponible', '0')
database['sq_meters'] = pd.to_numeric(database['sq_meters'], errors='coerce')
database['sq_meters'] = database['sq_meters'].fillna(0)

## 'available_from'
print(database['available_from'].value_counts())

## 'construction_year'
database['construction_year'] = database['construction_year'].replace('Non disponible', '0')
database['construction_year'] = pd.to_numeric(database['construction_year'], errors='coerce')

## 'property_type'
database['property_type'] = database['property_type'].astype('category')

## 'floor'
database['floor'] = database['floor'].str.replace('. étage', '')
database['floor'] = database['floor'].str.replace('Non disponible', 'not_available')
database['floor'] = database['floor'].str.replace('EG', 'ground_floor')
database['floor'] = database['floor'].str.replace('Untergeschoss', 'underground')
database['floor'] = database['floor'].astype('category')
print(database['floor'].value_counts())

## 'closest_shop'
database['closest_shop'] = database['closest_shop'].replace(',','')
database['closest_shop'] = database['closest_shop'].fillna(database.groupby("zip_code")['closest_shop'].transform("mean"))
database['closest_shop'] = database['closest_shop'].fillna(0)
database['closest_shop'] = pd.to_numeric(database['closest_shop'], errors='coerce')

## 'highway'
database['highway'] = database['highway'].replace(',','')
database['highway'] = database['highway'].fillna(database.groupby("zip_code")['highway'].transform("mean"))
database['highway'] = database['highway'].fillna(0)
database['highway'] = pd.to_numeric(database['highway'], errors='coerce')

## 'kindergarten'
database['kindergarten'] = database['kindergarten'].replace(',','')
database['kindergarten'] = database['kindergarten'].fillna(database.groupby("zip_code")['kindergarten'].transform("mean"))
database['kindergarten'] = database['kindergarten'].fillna(0)
database['kindergarten'] = pd.to_numeric(database['kindergarten'], errors='coerce')

## 'prim_school'
database['prim_school'] = database['prim_school'].replace(',','')
database['prim_school'] = database['prim_school'].fillna(database.groupby("zip_code")['prim_school'].transform("mean"))
database['prim_school'] = database['prim_school'].fillna(0)
database['prim_school'] = pd.to_numeric(database['prim_school'], errors='coerce')

## 'public_transp'
database['public_transp'] = database['public_transp'].replace(',','')
database['public_transp'] = database['public_transp'].fillna(database.groupby("zip_code")['public_transp'].transform("mean"))
database['public_transp'] = database['public_transp'].fillna(0)
database['public_transp'] = pd.to_numeric(database['public_transp'], errors='coerce')

## 'secon_school'
database['secon_school'] = database['secon_school'].replace(',','')
database['secon_school'] = database['secon_school'].fillna(database.groupby("zip_code")['secon_school'].transform("mean"))
database['secon_school'] = database['secon_school'].fillna(0) 
database['secon_school'] = pd.to_numeric(database['secon_school'], errors='coerce')


####
# Dummies
###

dummies = database[['parking_ext','parking_int','balcony','dishwasher','elevator','dryer','wash_m','tv']].fillna('0')
database = database.drop(['parking_ext','parking_int','balcony','dishwasher','elevator','dryer','wash_m','tv'], axis=1)
dummies = pd.get_dummies(dummies, columns=['parking_ext','parking_int','balcony','dishwasher','elevator','dryer','wash_m','tv'], 
            prefix=None ,drop_first=True, dtype="long")

database = pd.concat([database, dummies], axis=1)

### Property Types and floors
categorical_df = database.select_dtypes(include=['category']).copy()
print (database.head())

print (categorical_df['property_type'].value_counts())

property_type_df = pd.get_dummies(categorical_df, columns=['property_type'], prefix=["Type"], dtype="long")
print(property_type_df)

print(property_type_df.columns)

property_type_df.rename(columns={'Type_Appartement avec terrasse' : 'Type_Apartment_terrace',
                                 'Type_Appartement mansardé' : 'Type_Apartment_attic',
                                 'Type_Attique' : 'Type_Apartment_Penthouse',
                                 'Type_Autre' : 'Type_other',
                                 'Type_Ferme' : 'Type_Farm',
                                 'Type_Garage souterrain' : 'Type_Underground_garage',
                                 'Type_Immeuble' : 'Type_Multi_family house',
                                 'Type_Local commercial' : 'Type_Commercial_property',
                                 'Type_Local de bricolage' : 'Type_Hobby_room',
                                 'Type_Maison' : 'Type_Single_family_house',
                                 'Type_Maison en terrasse' : 'Type_Terraced_row_house',
                                 'Type_Maison mitoyenne' : 'Type_Split_level_house',
                                 'Type_Maison jumelée' : 'Type_Semi_detached_house',
                                 'Type_Terrain' : 'Type_Commercial_Land',
                                 'Type_Terrain à bâtir' : 'Type_Building_land',
                              }, inplace=True)

floor_df = pd.get_dummies(categorical_df, columns=['floor'], prefix=["floor"], dtype="long")
print(floor_df)
floor_df = floor_df.drop('property_type', 1)
print(floor_df.columns)

database = pd.concat([database, property_type_df, floor_df], axis=1)

database = database.iloc[: , :-39]
database = database.drop(['property_codes','address','available_from', 'prim_school',
              'floor','closest_shop','highway','kindergarten','public_transp','secon_school'], axis=1)


database.to_excel('GUI/gui_data/data.xlsx')


