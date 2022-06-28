import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

cvs_df = pd.read_csv('C:\\python39\\dataset_44_spambase.csv')
print(cvs_df)
target = cvs_df.pop('class')

rf = RandomForestClassifier(random_state=888)

rf.fit(cvs_df,target)
preds = rf.predict(cvs_df)
print(preds)
w = accuracy_score(target, preds)
print(w)