##  Reproduction of Simona Merlin IS 477 Final Project 
Simona Merlin - IS 477 Final project

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10291597.svg)](https://doi.org/10.5281/zenodo.10291597)

## Overview 

The dataset that is used in this project is the Online Retail data that accounts for all transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. It was donated to the UC Irvine Machine Learning repository on 11/5/2015. It includes 8 columns as well as 541,909 rows. The dataset includes columns of the invoice number, stock code, description of item, quantity of item, Invoice data, unit price, customer id, and the country that the transaction occurred. The feature types that were involved in the data was that of integers and real variables. There are no missing values within the dataset. The analysis that was done based off of this dataset was to find varying statistical findings from the Unit price column, which represents the product price per unit. Within this analysis, I found statistical findings of the count, mean, standard deviation, minimum, 25% quartile, 50% quartile, 75% quartile , and the maximum value of the unit price column. I wanted to look at these different statistics to see what are the trends within the product price per unit of these different transactions. 


## Workflow

Below is the DAG for the Snakemake workflow:

<img src ="workflow/graph.png" width ="200">

## Analysis 

I printed all of the relevant statistics needed in order to properly analyze the unit price column. The Unit price columns represent the product price per unit. From my findings, I found that on average, the product price per unit is 4.611114.  The most interesting findings that came from this statistical analysis is that there was a minimum -11,062.06. This is most likely an outlier due to the fact that an item would not have a negative price. Another interesting finding was that the maximum price per unit is 38,970.00. 


## Reproducing 

To reproduce the environment and run the script, follow the steps below.

1. Clone this repository

2.  Create a virtual encironement. All of my environment information will be found in the environment.log file

2. Install Dependencies: Make sure you have python and the required libraries installed:
Code: pip install -r requirements.txt. 
The requirements.txt contains the basic list of required libraries needed to reproduce.

3. Run the scripts to process and analyze the data
```
Code: python prepare_data.py 
Code: python profile.py
Code: python analysis.py
Code: python dag.py
```

4. Expected output:

```
count    541909.000000
mean          4.611114
std          96.759853
min      -11062.060000
25%           1.250000
50%           2.080000
75%           4.130000
max       38970.000000
Name: UnitPrice, dtype: float64
```


## License

This project uses the following licenses: 

```
Software license: MIT
Data License: CC-By-4.0

MIT - This permissive open source software license. This means that the license allows for the use and distribution of the code, but is giving me credit for creating the code. The MIT license is mainly used in the academic and research realm of software creation. 

```

## Refrences

Online Retail. (2015). UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

