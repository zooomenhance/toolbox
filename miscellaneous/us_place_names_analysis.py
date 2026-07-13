# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:31:17 2018

@author: adamclark
"""
####attempting to find the most common values in the USGS list of names of the US
   
##    "H:\TEST\us_place_names\usplacenames_subset.dbf"
##convert dbf to panda dataframe    

############################SANDBOX#######################################
##########################################################################
import pandas as pd

from simpledbf import Dbf5


dbf = Dbf5("H:/TEST/us_place_names/usplacenames_subset.dbf")
df_name = dbf.to_dataframe()

##find the most common value in the dataframe
df_mode = df_name.mode()
df_mode.head()
df_mode
##get the counts of each value
df_count = df_name.apply(pd.value_counts)
df_count.head()

df_countval = df_name
##identifying the series I want to count
df_name_series = df_name['NAME']
df_name_iloc = df_name.iloc[1],[1]
df_name_iloc.head()



##count the values and sort them by most frequent
df_name_series.value_counts(ascending=False)
## sort the datafram by the count column
df_name.sort_values(by=['NAME'])
## return top ten names


#####################################LIVE###################################


dbf = Dbf5("H:/TEST/us_place_names/usplacenames.dbf")
df_name = dbf.to_dataframe()
df_name_series = df_name['NAME']

df_name_series_count = df_name_series.value_counts(ascending=False)
df_subset = df_name_series_count.head(100)
df_subset
df_subset.plot.barh(figsize=(20,20))


#exclude the string "Church" if you want to only include a string remove the "~" sign from the function
##Can't figure out how to exclude multiple strings in the same function, so I just run it multiple times
df_nochurch = df_name[~df_name.NAME.str.contains("Church")]
df_nochurch = df_nochurch[~df_name.NAME.str.contains("Jehovah")]
df_nochurch = df_nochurch[~df_name.NAME.str.contains("School")]
df_nochurch = df_nochurch[~df_name.NAME.str.contains("Cemetery")]
df_name_nochurch_series = df_nochurch['NAME']
##
df_name_nochurch_series_count = df_name_nochurch_series.value_counts(ascending=False)
df_name_nochurch_series_count
df_subset = df_name_nochurch_series_count.head(100)
df_subset
df_subset_rv = df_subset.iloc[::-1]
df_subset_rv.plot.barh(figsize=(20,20))



df_subset_rv.plot.pie(figsize=(20,20))
