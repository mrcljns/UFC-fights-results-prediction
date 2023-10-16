# UFC-fights-results-prediction
This personal project focused on using Scrapy for scraping the data from ufcstats.com, ingesting it into a SQLite database and using it for predicting the results of UFC fights with machine learning models.
I figured this will be an interesting experiment as Ultimate Fighting Championship (or UFC) is the organizer of one of the biggest mixed martial arts events in the world, that attracts many people who speculate and bet on what the outcome of the match will be.
Based on features such as difference in height, weight, reach and age, I trained and tested four machine learning models.
The ROC AUC score of each of them is included in the table below:

Model | Random Forest | Logistic Regression | K Nearest Neighbors | XGBClassifier
--- | --- | --- | --- |---
ROC AUC score | 0.53 | 0.58 | 0.54 | 0.52

The results leave much room for improvement. It appears that genetic and age differences are not enough to determine the winner with confidence.
In the future I might extend the number of features with data on the win-loss ratio of a fighter right before the predicted fight.
