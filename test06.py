import pandas as pd
### Merge,Concat
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv',index_col= 0)
Ans = df
df1 = df.iloc[4:,:]
df2 = df.iloc[:4,:]

# Question 91
# df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
total = pd.concat([df1, df2])
Ans = total
# Question 92
# df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
df3 = df.iloc[:2,:4]
df4 = df.iloc[5:,3:]
total2 = pd.concat([df3,df4], join='inner')
Ans = total2
# Question 93
# df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
total3 = pd.concat([df3,df4], join='outer',).fillna(0)
Ans = total3
# uestion 94
# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
df5 = df.T.iloc[:7,:3]
df6 = df.T.iloc[6:,2:5]
merge_total = pd.merge(df5,df6, on='Algeria', how='inner')
Ans = merge_total
# Question 95
# df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
merge_total2 = pd.merge(df5,df6,on='Algeria', how='outer')
Ans= merge_total2
print(Ans)