# UFC-fights-results-prediction
## Synopsis
Are you a fan of UFC or MMA? If yes, you must have wondered at some point - do genetic factors like height and reach matter during MMA fights? Or maybe - do younger fighters outperform the older ones? Well, either that or you like betting and predicting UFC fights result and are looking for some way to increase your chances. In this python project I've tried to answer the above questions and the answers are...interesting to say the least. Of course, the only explanatory variables at my disposal are differences in height, reach and age between fighters. Out of the three binary classification models I've used, Logistic regression with l2 regularization gave the best results of 0.6 ROC AUC score and 0.57 accuracy score. It's still a poor performence as there are many other factors, which are more complicated to include (for example number of wins before a certain fight). Nevertheless, it's more than a completely random guess and gives some insight into what determines the winner of a MMA fight.

This repository includes both a webscrapper of data from ufcstats.com, as well as a Jupyter Notebook containing the machine learning models. To scrap the data, I employed the Scrapy framework. The Scrapy pipeline uses SQLite to save the data into a database consisting of fight data (event, winner, loser) and individual fighter stats (height, weight etc.). After merging datasets and some data cleaning and processing, the .ipynb file is ready to used.

## File Description
* ufc.scrapy.py: Scrapy spider that scraps data from ufcstats.com
* pipelines.py: Scrapy pipeline, which saves data to a database using SQLite
* ufc_data.csv: the file I used for developing the predictions
* ufc_ml_proc.py: code for cleaning and processing the data
* ufc_ml_analysis.ipynb: Jupyter Notebook where I did the analysis and model training
