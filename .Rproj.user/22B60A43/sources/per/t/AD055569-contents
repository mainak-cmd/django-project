import pandas as pd
df=pd.read_csv("diabetes.csv")
df.head

def na_remove(data,i):
  d1=pd.DataFrame(data.isnull().sum(),columns=['na_count'])
  for (row,rowdata) in d1.iterrows():
    if int(rowdata["na_count"])>i:
      print(row)
 
#feature haveing na value that grater than 50% of sample      
na_remove(df,384)
#feature haveing na value that grater than 0 
na_remove(df,0)

import lazypredict

#useing R to determine influence point ,hypothisis testing for normality
import lazypredict
from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
