import numpy as np
from sklearn.cluster import MeanShift, KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import tree
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df = pd.read_csv('July19_myspeed.csv',nrows=10000)
original_df = pd.DataFrame.copy(df)
#df.fillna(-9999,inplace=True)
df = df.dropna()
df['signal_strength'] = df['signal_strength'].apply(lambda x: x*-1)
df['Service_provider']=le.fit_transform(df['Service_provider'])
df['technology']=le.fit_transform(df['technology'])
df['Download_Upload']=le.fit_transform(df['Download_Upload'])
df['Service_Area']=le.fit_transform(df['Service_Area'])

print(df.head())
X = np.array(df.drop(['Data_Speed.Kbps.'], 1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['Data_Speed.Kbps.'])
# #clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=13,verbose=1)
# # clf = tree.DecisionTreeClassifier()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = svm.SVC(gamma='scale')
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
# plt.scatter(X_train, y_train,  color='black')