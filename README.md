# Brands

this simple application show data about the global brands and super bowl ads.


## Brand table

name = name of brands.

value = Brand Value (US$ Mil.).

Change = Brand Value Change vs 2020.

Origin = Market of Origin.


## ads table

name = name of brands's ads that get superbowl.

Year = year that get superbowl.

Danger = is the ads danger or not.

Url = url link of ads.


## How to run

#### create database using schema commands in a file

sqlite3 brands.db < brands.schema


#### then import data from a CSV file.

sqlite> .mode csv

sqlite> .import data/GlobalBrands.csv brands

sqlite> .import data/superbowl-ads.csv ads