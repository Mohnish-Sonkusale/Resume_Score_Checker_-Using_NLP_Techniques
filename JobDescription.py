import Preprocessing
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/srbhr/Naive-Resume-Matching/master/Job_Data.csv', on_bad_lines='skip')
#print(df.head())

df1 = df[['Name','Context']]
df1['Name'] = df1['Name'].apply(lambda x : x.split('.')[0])
df1['preProcessed'] = df1['Context'].apply(lambda x : Preprocessing.TextPreprocessing(x))
df1['Context'] = df1['Context'].apply(lambda x : Preprocessing.removeslashn(x))
#print(df1.columns)
df1.to_csv('JobDesCleaned.csv')