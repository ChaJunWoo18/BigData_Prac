import pandas as pd
#DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
#df = pd.read_csv(DataUrl, sep="\t")
#df.head()
#print(df.shape)
#print("행",df.shape[0],"열",df.shape[1])
#print(df.columns)
#print(df.columns[5])
#print(df.loc[:,df.columns[5]].dtype) # print(df.iloc[:,5].dtype)
#print(df.index)
#print(df.iloc[2,5])
#DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'
#df = pd.read_csv(DataUrl, encoding='cp949') #euc-kr, utf-8
#print(df)
#df.tail(3)
#print(df.select_dtypes(exclude=object).columns)
#print(df.select_dtypes(include=object).columns)
#print(df.isnull().sum())
#df.info()
#df.describe()
#print(df['거주인구'])
#print(df['평균 속도'].quantile(0.75) - df['평균 속도'].quantile(0.25))
#print(df['읍면동명'].nunique())
#print(df['읍면동명'].unique())
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv')
#print(df[df['quantity']==3].head())
#print(df[df['quantity']==3].head().reset_index(drop=True))
ans = df[['quantity','item_price']]
df['new_price'] = df['item_price'].str[1:].astype('float')
#print(df.head())
ans = df.loc[df['new_price']<=5]
#print(len(ans))

#print(df.loc[df['item_name']=='Chicken Salad Bowl'].reset_index(drop=True))
#print(df.loc[(df['new_price']<=9) & (df['item_name']=='Chicken Salad Bowl')])
#print(df.sort_values('new_price').reset_index(drop=True))
#print(df.loc[df['item_name'].str.contains('Chips')])
#print(df.iloc[:,::2].head())
#print(df.sort_values('new_price',ascending=False).reset_index(drop=True))
#ans = df.loc[(df['item_name']=='Steak Salad') | (df['item_name']=='Bowl')]
#ans = ans.drop_duplicates('item_name')
#ans = ans.drop_duplicates('item_name', keep='last')
#print(ans)
#print(df.loc[df['new_price'] >= df['new_price'].mean()].head()) #35
#####################################35######################################
#df[df['item_name']=='Izze']['item_name'] = 'FIzzy Lizzy'
#print(df.head())
#37
#print(df['choice_description'].isnull().sum())
#38
#df.loc[df['choice_description'].isnull()]['choice_description']='No Data'
#print(df.head())
#39 -- notnull을 사용해서 결측치를 제거해야한다. 결측치는 float이기 때문에 str을 사용X
#Ans = df.loc[df['choice_description'].notnull() & df['choice_description'].str.contains('Black')]
#print(Ans.head())
#40 - 문자의 길이는 len() 또는 shape
ans = df.loc[~(df['choice_description'].notnull() & 
            df['choice_description'].str.contains('Vegetables'))].shape[0]
#print(ans)
#41
#print(df[df['item_name'].str[0]=='N'].head())
#print(df[df['item_name'].str.startswith('N')].head())
#42
#print(df[df['item_name'].str.len() >=15].head())
#43
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
#print(df[df['new_price'].isin(lst)])
#print(len(df[df['new_price'].isin(lst)]))
