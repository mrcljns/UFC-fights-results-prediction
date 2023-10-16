import pandas as pd
import re
import datetime
import numpy as np

r = re.compile(r"([0-9]+)' ([0-9]*\.?[0-9]+)\"")

def get_inches(el):
    """
    Converts distance in feet to inches
    """
    m = r.match(el)
    if m == None:
        return float('NaN')
    else:
        return int(m.group(1))*12 + float(m.group(2))

# Importing data
ufc_data = pd.read_csv('ufc_data.csv', sep =';')

ufc_data['win'] = 0

# Getting rid of missing values
ufc_data = ufc_data.dropna()
ufc_data = ufc_data.loc[(ufc_data['reach'] != '--') & (ufc_data['l_reach'] != '--')]

# Setting half of data to 1
half = int(len(ufc_data['win'])/2)
ufc_data['win'][:half] = 1

# Change explanatory variables into integers
ufc_data['height'] = [get_inches(x) for x in ufc_data['height']]
ufc_data['l_height'] = [get_inches(x) for x in ufc_data['l_height']]

ufc_data['weight'] = [int(re.sub("[^0-9]", "", x)) for x in ufc_data['weight']]
ufc_data['l_weight'] = [int(re.sub("[^0-9]", "", x)) for x in ufc_data['l_weight']]

ufc_data['reach'] = [int(re.sub("[^0-9]", "", x)) for x in ufc_data['reach']]
ufc_data['l_reach'] = [int(re.sub("[^0-9]", "", x)) for x in ufc_data['l_reach']]

ufc_data['bday'] = [datetime.datetime.strptime(x, '%b %d, %Y') for x in ufc_data['bday']]
ufc_data['l_bday'] = [datetime.datetime.strptime(x, '%b %d, %Y') for x in ufc_data['l_bday']]

# Computing the differences between explanatory variables of the winner and the loser
ufc_data['diff_h'] = ufc_data['height'] - ufc_data['l_height']
ufc_data['diff_w'] = ufc_data['weight'] - ufc_data['l_weight']
ufc_data['diff_r'] = ufc_data['reach'] - ufc_data['l_reach']
ufc_data['diff_byear'] = ufc_data.bday - ufc_data.l_bday
ufc_data['diff_byear'] = ufc_data.diff_byear / np.timedelta64(1, 'Y')

ufc_ml_df = ufc_data[['win', 'winner', 'loser', 'diff_h', 'diff_w', 'diff_r', 'diff_byear']]

# Switching explanatory variables from winner's perspective to loser's perspective
ufc_ml_df.loc[ufc_ml_df['win']==0, ['diff_h', 'diff_r', 'diff_w', 'diff_byear']] *= (-1)

ufc_ml_df.reset_index(drop=True)

# Exporting to csv
ufc_ml_df.to_csv('ufc_ml_df.csv', sep=';', index = False)