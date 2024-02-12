import pandas as pd

# Use the correct parameter name 'delimiter' and specify '\t' for tab delimiter
df = pd.read_csv('C:/Users/parim/OneDrive/Desktop/New folder/pokemon.csv', delimiter='\t')

print(df.head(3))

# read header

print(df.columns)

#read each column

print(df['name'][0:5])

print(df[['Name','Type 1','HP']])

#read each row

print(df.iloc[1:4])#integer location

for index, row in df.iterrows():
    print(index, row['Name'])
    
df.loc[df['Type 1']=="Fire"]

df.describe()

df.sort_values(['Type 1','Name','HP'],ascending=[1,0,0]) #we want first ascending and the both descending

df.head(5)

