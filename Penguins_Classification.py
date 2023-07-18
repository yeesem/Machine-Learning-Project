import pandas as pd

penguins = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/code/master/streamlit/part3/penguins_cleaned.csv")

#Print the first 5 rows of the dataset
#print(penguins.head())

#Original features encoding
df = penguins.copy()
target = 'species'

#sex and island are the names of the column
encode = ['sex','island']

#Split the data in the both columns into new column and do binary assignment
for col in encode:
    dummy = pd.get_dummies(df[col],prefix=col)
    df = pd.concat([df,dummy],axis=1)
    del df[col]

target_mapper = {'Adelie':0,'Chinstrap':1,'Gentoo':2}
def target_encode(val):
     return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

#Separating X and Y
X = df.drop('species',axis=1)
Y = df['species']

#Build random forest model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X,Y)

#Saving the model
#wb stands for write binary
import pickle
pickle.dump(clf,open('penguins_clf.pkl','wb'))
