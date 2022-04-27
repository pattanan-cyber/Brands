# Brands

this simple application show data about the global brands and super bowl ads.


## Brand table

brand = name of brands.

value = Brand Value (US$ Mil.).

Change = Brand Value Change vs 2020.

category = category of brands.

Rank_change = Rank change.

Origin = Market of Origin.


## ads table

Year = year that get superbowl.

brand = name of brands's ads that get superbowl.

Url = url link of ads.

youtube_url = url youtube link of ads.

funny  = is the ads funny or not.

show_product_quickly = is the ads show product quickly or not.

patriotic = is the ads has patriotic or not.

celebrity = is the ads has celebrity or not.

Danger = is the ads has danger or not.

animals = is the ads has animals or not.

use_sex = is the ads use sex or not.


## How to run

#### install package.

pip install -r requirements.txt

#### create database using schema commands in a file.

sqlite3 brands.db < brands.schema


#### then import data from a CSV file.

sqlite> .mode csv

sqlite> .import data/GlobalBrands.csv brands

sqlite> .import data/superbowl-ads.csv ads