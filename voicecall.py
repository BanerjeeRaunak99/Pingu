import numpy as np
# from sklearn.cluster import MeanShift, KMeans
# from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('MyCall_Data_February_2019_Final_1.csv')
original_df = pd.DataFrame.copy(df)
df.drop(['In Out Travelling','State 2me'], 1, inplace=True)
def handle_non_numerical_data(df):
    
    # handling non-numerical data: must convert.
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        #print(column,df[column].dtype)
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            
            column_contents = df[column].values.tolist()
            #finding just the uniques
            unique_elements = set(column_contents)
            # great, found them. 
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    # creating dict that contains new
                    # id per unique string
                    text_digit_vals[unique] = x
                    x+=1
            # now we map the new "id" vlaue
            # to replace the string. 
            df[column] = list(map(convert_to_int,df[column]))

    return df
df = handle_non_numerical_data(df)
X = np.array(df.drop(['Call Drop Category'], 1).astype(float))
# X = preprocessing.scale(X)
y = np.array(df['Call Drop Category'])
# clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0,verbose=1)
clf = tree.DecisionTreeClassifier()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
example_measures = np.array([3,1,1,29.994077,76.9527568])
example_measures = example_measures.reshape(1, -1)
prediction = clf.predict(example_measures)
print(prediction)


