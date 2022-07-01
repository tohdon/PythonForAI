from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score

features, target = load_wine(return_X_y=True)
rf_model = RandomForestClassifier(random_state=1)
rf_model.fit(features, target)
print(features)
print(target)
preds= rf_model.predict(features)
print(preds)

acc = accuracy_score(target, preds)
print("accuracy score:", acc)