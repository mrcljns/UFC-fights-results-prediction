from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot
from collections import Counter

ufc_ml_df = pd.read_csv('ufc_ml_df.csv', sep=';')

#Descriptive statistics
#print(ufc_ml_df.describe())

#The result is whether the fighter won
result = np.array(ufc_ml_df['win'])

counter = Counter(result)

ufc_ml_df = ufc_ml_df.drop(['win', 'winner', 'loser'], axis=1)

ufc_ml_list = list(ufc_ml_df.columns)

expl = np.array(ufc_ml_df)

#Plots
#for label, _ in counter.items():
#	row_ix = np.where(result == label)[0]
#	pyplot.scatter(expl[row_ix, 0], expl[row_ix, 2], label=str(label))
#pyplot.legend()
#pyplot.show()

#splitting data
train_ufc, test_ufc, train_result, test_result = train_test_split(expl, result, test_size = 0.3, random_state = 50)




#RANDOM FOREST
#----------------------------------------------------------------------

#Checking the shapes of data after splitting
#print('Training UFC dataset Shape:', train_ufc.shape)
#print('Training Result Shape:', train_result.shape)
#print('Testing UFC dataset Shape:', test_ufc.shape)
#print('Testing Result Shape:', test_result.shape)

rf = RandomForestClassifier(n_estimators=100, bootstrap = True, max_features=None)

rf.fit(train_ufc, train_result)

predictions = rf.predict(test_ufc)
errors = abs(predictions - test_result)

rf_probs = rf.predict_proba(test_ufc)[:, 1]
roc_value = roc_auc_score(test_result, rf_probs)

print('Mean Absolute Error:', round(np.mean(errors), 2))
print('ROC AUC:', round(np.mean(roc_value), 2))




#LOGISTIC REGRESSION
#-----------------------------------------------------------------------------------------
log_model = LogisticRegression(solver='liblinear', C=10, random_state=0)
log_model.fit(train_ufc, train_result)
log_predictions = log_model.predict(test_ufc)
print("Logistic model score: ", log_model.score(test_ufc, test_result))
print(confusion_matrix(test_result, log_predictions))

#Confusion matrix heat map
cm_log = confusion_matrix(test_result, log_predictions)

fig, ax = pyplot.subplots(figsize=(8, 8))
ax.imshow(cm_log)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm_log[i, j], ha='center', va='center', color='red')
pyplot.show()




#K NEAREST NEIGHBOURS
#----------------------------------------------------------------------------------
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(train_ufc, train_result)
knn_predictions = knn.predict(test_ufc)

cm_neighbour = confusion_matrix(test_result, knn_predictions)
print(cm_neighbour)

ufc_ml_df

