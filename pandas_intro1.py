import pandas as pd

data = {
    'Country'   :   ['Belgium', 'India', 'Brazil'],
    'Capital_city' :   ['Brussels', 'New_Dehli', 'Brasilia'],
    'Population'    :   [11190846, 1303171035, 207847528]
}

df1 = pd.DataFrame(data, columns = ['Country', 'Capital_city', 'Population'])


dfFila = df1.ix[2]

print(df1.ix[0,'Country'])

print(df1[df1['Population']>2e7])

print(df1['Population'].mean())
f = lambda x:x*0.5

df1['half_pop'] = df1['Population'].apply(f)
print(df1)