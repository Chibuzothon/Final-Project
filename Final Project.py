#Final Project
#Incorporate pandas & matplotlib, git and regular expressions 

#add what is required to readme, check class powerpoint & files



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#loaded the path of the table as a csv file, read the file and then printed the table.
house_prices_path = "C:/Users/Maryl/OneDrive/Desktop/Final Project/American_Housing_Data_20231209.csv"
house_prices = pd.read_csv(house_prices_path)
print(house_prices)
#used describe method to get statistical analysis of the values in each column/series
house_prices.describe()


#looked at the colunms and rows in the table where the total beds in the house is less than 9
#counts the number of houses that has beds that are less than 9
#saved that data into a df
df_house_price = house_prices[house_prices["Beds"]<9] 
#house_prices["Beds"] represents all the values in the column. 
#house_prices["Beds"]<9 considers the Beds column, will return True for where the beds is less than 9
#house_prices[house_prices["Beds"]<9] table info (rows & coulums) where the beds is less than 9 

#used a histogram to plot the df 
#histogram plots the beds column of the table 
plt.hist(df_house_price["Beds"]) #specifies the column to look at
plt.show()


#created a df of the number of beds less than 9, and the price 
#takes the average prices of the houses based on number of beds
df_prices_by_beds =df_house_price[["Beds","Price"]].groupby(["Beds"]).mean() 
#values of index, put into a column. Because the beds count is an index in the df
df_prices_by_beds["Bed_count"] = df_prices_by_beds.index 
#plotted a bar graph for the bed count, (where rooms is less than 9) vs the average price of the houses 
plt.bar(x="Bed_count", height="Price", data = df_prices_by_beds)   
plt.show()
print(df_prices_by_beds)


#loaded the path of a csv file, read the file, & then printed the table
afro_spotify_path = "C:/Users/Maryl/OneDrive/Desktop/Final Project/spotifyafro.csv"
afro_spotify = pd.read_csv(afro_spotify_path)
print(afro_spotify)


#Regular expression & indexing to print out the row of data where "boy" shows up in the artist name
#/b == "word boundary"
# [] only one option, lower or uppercase b
artist_pattern = r".*[bB]oy/b" #matches anything that has boy or Boy .* = matches anything

Boy_artist_name = afro_spotify[afro_spotify["artist"].str.match(artist_pattern)] #column/series
# afro_spotify.loc[(afro_spotify["artist"] == "Burna Boy")]
print(Boy_artist_name)
Boy_artist_name.artist.unique() #returns the names of the artists that have boy in their name
