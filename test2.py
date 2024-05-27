import pandas as pd
#44
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv')
#45 - size는 group별 빈도수를 계산(NaN값을 포함한다)
#Ans = df.groupby('host_name').size().reset_index().sort_values(by='host_name')
#Ans.columns = ['host_name','count']
#or
#Ans = df.value_counts("host_name").reset_index().sort_values(by='host_name')
#46 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 
#    빈도수 컬럼은 counts로 명명하라'''
Ans = df.value_counts('host_name').to_frame('counts').sort_values(by='counts', ascending=False)
#47 neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라'''   
#valuecounts는 기본값이 내림차순이며, size는 정렬하지 않는다. value_counts의 옵션에 sort=False도 있다.
Ans = df.groupby('neighbourhood_group', as_index=False)['neighbourhood'].value_counts()
Ans = df.groupby(['neighbourhood_group','neighbourhood'],as_index=False).size()
#48 neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 
#neighbourhood_group그룹의 최댓값들을 출력하라'''
Ans = df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size()\
    .groupby(['neighbourhood_group'], as_index=False).max()
#'''49 neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라'''
Ans = df[['neighbourhood_group','price']]\
    .groupby('neighbourhood_group').agg(['mean','var','max','min'])
#'''50 neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라'''
Ans = df[['neighbourhood_group', 'reviews_per_month']]\
    .groupby('neighbourhood_group').agg(['mean','var','max','min'])
#''51 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라'''
Ans = df.groupby(['neighbourhood','neighbourhood_group'])['price'].mean()
#''52 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라'''
Ans = df.groupby(['neighbourhood','neighbourhood_group'])['price'].mean().unstack()
#'' 53 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고 
#nan 값은 -999값으로 채워라''' #unstack(fill_value=-999) 도 있따.
Ans = df.groupby(['neighbourhood','neighbourhood_group'])['price'].mean().unstack().fillna(-999)
#'''54 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 
#neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라'''
Ans = df[df['neighbourhood_group']=='Queens'].\
    groupby('neighbourhood')['price'].agg(['mean','var','max','min']).head()
#55 데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고 
#neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라 ******
Ans = df[['neighbourhood_group', 'room_type']].groupby('neighbourhood_group')\
    ['room_type'].value_counts().unstack()
Ans.loc[:,:] = Ans.values / Ans.sum(axis=1).values.reshape(-1,1)
print(Ans)
