import seaborn as sns
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import patsy
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
from statsmodels.graphics.correlation import plot_corr
from sklearn.model_selection import train_test_split
plt.style.use('seaborn')
rawdata= pd.read_csv('C:\\software\\python\\Boston.csv')
print(rawdata)
rawdata = rawdata.dropna()
rawdata = rawdata.drop_duplicates()
print(list(rawdata.columns))
print(rawdata.describe(include=[np.number]).T)

X = rawdata.drop('CRIM', axis=1)
Y = rawdata[['CRIM']]
seed = 10
test_data_size = 0.3
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size= test_data_size, random_state=seed)
train_data = pd.concat([x_train, y_train], axis=1)
test_data_= pd.concat([x_test, y_test], axis=1)

corrMatrix = train_data.corr(method='pearson')
xnames = list(train_data.columns)
ynames = list(train_data.columns)
#plot_corr(corrMatrix, xnames=xnames, ynames=ynames, title=None, normcolor=False,cmap='coolwarm')
#corr.style.background_gradient(cmap='coolwarm')

fg, ax= plt.subplots(figsize=(10,6))
sns.regplot(x='MEDV', y='CRM', ci=None,data=train_data, ax =ax, color='k', scatter_kws={"s" : 20, "color": "royalblue", "alpha": 1})
ax.set_ylabel('Crimerate per Capita', fontsize=15, fontname='DejaVu Sans')
ax.set_xlabel('Median value of owner-occupied homes in $1000', fontsize=15, fontname='DejaVu Sans')
ax.set_xlim(left=None, right=None)
ax.tick_params(axis='both', which='major', labelsize=12)
fig.tight_layoout()
