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
#loc-row and column name
#iloc-row and column indexes

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the column using the name

df.loc[0, 'Salary']

# To make the name column as the index using set_index() and saving it to a new dataframe
df2=df
df2=df2.set_index("Name")

#Slicing

df.loc[2:3,'Name':'Department']
df.iloc[0:3,1:3]


#to make a list as index unsing index() function
new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
df_new.loc['a','Artist']
df_new.loc['a':'d','Artist']
