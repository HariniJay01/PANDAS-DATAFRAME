import pandas as pd
dict1={'Student':['David','Samuel','Terry','Evan'],
       'Age':['27','24','22','32'],
       'Country':['UK','Canada','China','USA'],
       'Course':['Python','Data Structures','Machine Learning','Web Development'],
       'Marks':['85','72','89','76']}
df1 = pd.DataFrame(dict1)
df1

# Retrieve the Marks column and assign it to a variable b as "dataframe"
b=df1[['Marks']]
b

#Retrieve the Country and Course columns and assign it to a variable c
c=df1[['Country','Course']]
c

# Retrieve the Marks column and assign it to a variable b as "series"
b=df1['Marks']
b
