from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

features, target = load_breast_cancer(return_X_y=True)

print(features)
print(target)
seed = 888
rf_model = RandomForestClassifier(random_state=seed)
rf_model.fit(features, target)
preds= rf_model.predict(features)

print("prediction")
print(preds)

acc = accuracy_score(target, preds)
print("accuracy score:", acc)