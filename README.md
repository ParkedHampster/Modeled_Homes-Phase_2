# Modeled_Homes-Phase_2
Data understanding of the King County housing market based on available data


```
Modeled_Homes-Phase_2
├── code
├── data
│  ├── column_names.md
│  └── kc_house_data.csv
├── img
├── index.ipynb
├── individual_notebooks
│  ├── anat.ipynb
│  ├── code -> ../code
│  ├── data -> ../data
│  ├── img -> ../img
│  ├── jd.ipynb
│  └── README.md
├── LICENSE
└── README.md
```


# who is our audience? 
- We are going to look at how zip code effect prices (how everything within zip code effects price)
- Removing those not in king county based on our new CSV
- Speaking to individuals looking to buy homes within kings county 

# Data Cleaning
What are we removing?
 - Removing lat, long, 
 - Added zip -- merged zip (add in link to where we got the data from)

- maybe add categorical column off of porch and so on
- note the outliers in price
- excluding below 400 sqr ft living bc not looking for tiny home 
- greater than 0 bedrooms, looking for a place with bedroom
- bathroom greater than 0 
- Adding boolean columns for has porhc, waterfront, basement