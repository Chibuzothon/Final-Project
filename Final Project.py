#Final Project
#Incorporate pandas, matplotlib, git and regular expressions, to analyze data from a csv table 

import pandas as pd
import matplotlib.pyplot as plt


#House Prices Analysis

#loaded the path of the table as a csv file, read the file and then printed the table.
house_prices_path = "C:/Users/Maryl/OneDrive/Desktop/Final Project/American_Housing_Data_20231209.csv"
house_prices = pd.read_csv(house_prices_path)
print(house_prices)
#used describe method to get statistical analysis of the values in each column/series
house_prices.describe()


#looks at the colunms and rows in the table where the total bedrooms in the house is less than 9
#saved that data into a df
#house_prices[house_prices["Beds"]<9] table info (rows & coulums) where the beds is less than 9 
df_house_price = house_prices[house_prices["Beds"]<9] 


#used a histogram to plot the df 
#histogram plots the beds column of the table 
plt.hist(df_house_price["Beds"]) #specifies the column to look at
plt.show()


#created a df of the number of bedrooms that are less than 9, and the price 
#takes the average prices of the houses based on number of bedrooms 
df_prices_by_beds =df_house_price[["Beds","Price"]].groupby(["Beds"]).mean() 
#puts index values into a column, because the bedroom count is an index in the df
df_prices_by_beds["Bed_count"] = df_prices_by_beds.index 

#plotted a bar graph for the bedroom count, (where bedroom is less than 9) vs the average price of the houses 
plt.bar(x="Bed_count", height="Price", data = df_prices_by_beds)   
plt.show()
print(df_prices_by_beds)



#Spotify Artist Analysis 

#loaded the path of a csv file, read the file, & then printed the table
afro_spotify_path = "C:/Users/Maryl/OneDrive/Desktop/Final Project/spotifyafro.csv"
afro_spotify = pd.read_csv(afro_spotify_path)
print(afro_spotify)


#Regular expression & indexing to print out the row of data where "Boy" or "boy" shows up in the artist name
#/b == "word boundary"
# [] only one option, lower or uppercase b
#matches anything that has boy or Boy .* = matches anything
artist_pattern = r".*[bB]oy\b" 

Boy_artist_name = afro_spotify[afro_spotify["artist"].str.match(artist_pattern)]
#Displays the columns and rows for the artists that have "Boy" in "boy" in their name
print(Boy_artist_name)
#returns the names of the artists that have "Boy" or "boy" in their name
Boy_artist_name.artist.unique() 
