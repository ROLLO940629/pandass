import numpy as np
import pandas as pd
df = pd.read_excel (r'C:\Users\abdou\Desktop\pandas\les_ventes_df.xlsx')
print (df.head(5))

print(df.columns)
print(df.shape)
df=df.drop(['Unnamed: 0','PIECE','FOLIO','N° LIGNE','COCHE'],axis=1)
print(df.columns)

df2=pd.pivot_table(df,
             values=['DEBIT','CREDIT'],
              index=['REFERENCE','DATE'],
              columns='COMPTE',
            aggfunc=np.sum, margins=True
              )
print(df2.head(5))
df2=df2.loc[(df2.sum(axis=1) != 0), (df2.sum(axis=0) != 0)]

print(df2.isnull().values.sum())
df2=df2.fillna(0)
print(df2.isnull().values.sum())
# df2.loc["total"]=df2.sum(axis=1)
print(df2.columns)
idx = pd.IndexSlice
df2=df2.drop(df2.loc[:,idx[:,'All']],axis=1)




# df2.loc[:,idx[:,'DATE']]=df2.loc[:,idx[:,'DATE']].dt.strftime('%m/%d/%Y')
# print(df['DATE'].dtypes)

df2.to_excel(r'C:\Users\abdou\Desktop\pandas\pivote.xlsx')