#Final Project 

#don't worry about fundamentals focus on adavanced topics 
#incoporate numpy/pandas/matplotlib
#incorporate git
#incorporate regular expressions


#questions to ask
#how to add git
#adding regular expressions
#ways I can incoporate numpy
#add readme 
# add license
#question about getting an A+, do I completed the peer review & presented my code, do I need to complete more particpation?


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#loaded the path of the table as a csv file, read the file and then printed the table
house_prices_path ="C:/Users/Maryl/Downloads/INST126/American_Housing_Data_20231209.csv"
house_prices = pd.read_csv(house_prices_path)
print(house_prices)
house_prices.describe()

df_house_price = house_prices[house_prices["Beds"]<9] #house_prices["Beds"] represents all the values in the column. 
# house_prices[house_prices["Beds"]<9] table info where the beds is less than 9
# house_prices["Beds"]<9 considers the Beds column, will return True for where the beds is less than 9
plt.hist(df_house_price["Beds"]) #specifies the column to look at
plt.show()


df_prices_by_beds =df_house_price[["Beds","Price"]].groupby(["Beds"]).mean() #gets the df of the Beds and price & groups by beds Then takes the average price based on number of beds
df_prices_by_beds["Bed_count"] = df_prices_by_beds.index #values of index, put into a column. Bc the beds count is an index in the df
plt.bar(x="Bed_count", height="Price", data = df_prices_by_beds) #plots the bed count vs the average price of the house
# df_prices_by_beds.index      
plt.show()
print(df_prices_by_beds)




#want to plot the average house space vs the average cost
#scatter plot to see the relationship between the house space and the price of the house
plt.scatter("Living Space", "Price", data = house_prices)
plt.show()

plt.plot("Living Space", "Price", data = house_prices)
plt.show()


#loaded the path of a csv file, read the file then printed the table
afro_spotify_path = "C:/Users/Maryl/Downloads/INST126/spotifyafro.csv"
afro_spotify = pd.read_csv(afro_spotify_path)
print(afro_spotify)


#Regular expression & indexing to print out the row of data were the artist has the name boy
#\b == "word boundary"
artist_pattern = r".*[bB]oy\b" #matches anything that has boy or Boy .* = matches anything
# [] only one option, lower or uppercase b
# df_afro_spotify = afro_spotify[afro_spotify["artist"]] 
# print(df_afro_spotify)
# df_afro_artist = afro_spotify["artist"] #acess the artist colunm within the afro spotify table
# print(df_afro_artist) #prints out the names of all the artists in the table
Boy_artist_name = afro_spotify[afro_spotify["artist"].str.match(artist_pattern)] #column/series
# afro_spotify.loc[(afro_spotify["artist"] == "Burna Boy")]
print(Boy_artist_name)
Boy_artist_name.artist.unique() #retunrs the naes of the artists that have boy in their name

