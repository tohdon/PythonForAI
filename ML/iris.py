from sklearn.datasets import load_iris
from IPython.display import display
import pandas as pd
import seaborn as sns
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
display(pd.concat([iris_df.head(3), iris_df.tail(3)]))
sns.pairplot(iris_df, hue='target', height=1.5)
print('targets: {}'.format(iris.target_names), iris.target_names[0], sep="\n")
