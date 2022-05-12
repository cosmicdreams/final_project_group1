# Team-group1  - Technology.md Document
### Chris Weber, Elder Arias, Terra Lasho, Pierre Boucard, and Thaofeeqat Dauda
## Introduction: 
- This document provides a checkpoint, a first ‘planned sketch’ including a brief description of our technological intentions as we navigate this project.  So far, our group has narrowed down project ideas to 2, and as we continue this week to our final choice, we will delineate the needs/pathway for each below:
### Potential Project Idea 1: Dow Jones Index Daily Performance by US Atmospheric Influence
### Summary:
-	Use machine learning to analyze Down Jones historical performance and US weather (major cities) to determine if there is association/influence by the weather or if any other correlations can be completed.
#### Questions we want to answer:
- Does the US daily average weather have influence over DJI's performance (using dataset containing daily performance from 1992 to 2022; and archived US weather from NWA)?
- Can we PREDICT a positive DJI timeframe by using weather forecasting?
### Datasets:
-	At least two different datasets are required for this project: DJI historical performance and Historical weather from US major cities.
-	DJI Dataset:
o	1992 to 2022
	https://finance.yahoo.com/quote/%5EDJI/history/
-	Weather Dataset:
o	https://kilthub.cmu.edu/articles/dataset/Compiled_daily_temperature_and_precipitation_data_for_the_U_S_cities/7890488?file=32874374






### Potential Project Idea 2: Scanning a pokemon: Team balance recommendation - Notable pokemon near you (using multiple large pokemon stat datasets; large pokemon image dataset; geographic location dataset for specific pokemon features)!

### Summary:
- Use machine learning in several different ways to interrogate Pokemon datasets, which include images, characteristics and geographical location. We will form an image classifier, a recommendation system incorporating geographic locations for finding pokemon, and a prediction model concerning characteristics.


#### Questions we want to answer: 
- Can we create a pokemon image classifier?
- Can we predict the type of pokemon based on having a gender vs. not?
- Can we provide recommendation for notable pokemon by requested location?

## Technologies Used:
-	Software: Jupyter Notebook, and Python 3.7.9
-	Python libraries:
- Numpy
- Pandas
- Seaborn (violin, factorplot, heatmap)
- Matplotlib
- Graphvis (for graphic visualization)
- Scikit-Learn

## Data Cleaning and Analysis
-	Pandas will be used to clean the data and perform an exploratory analysis. First we will import our CSV files into a pandas dataframe. Next, we will loop through the data using pandas and convert and transform the categorical data (LabelEncoder and pandas). We will next clean the data by dropping rows with missing values, or filling in the row that has a missing value. Finally, we will merge the datasets to be used for analysis.
-	Numpy will be used for linear algebra and fixing arrays, Seaborn for cool visualizations, matplotlib for figures, graphviz for awesome graph visualization and Scikit-Learn for preprocessing and machine learning algorithms.
-	Postgres will be used for data storage.
-	Several project specific tools may include:

## Dashboard
-	TBD, however, we are interested in using Tableau, and plotly.js. We will potentially deploy our dashboard to a cloud server.
## Machine Learning Model:
-	Classification or Regression predictive modeling can be used with this dataset:
o	Classification is the task of predicting a discrete class label.
o	Regression is the task of predicting a continuous quantity.
