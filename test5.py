import pandas as pd
### Pivot
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv')
Ans = df.head()

#Question 83
#Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
df.drop('Indicator',axis=1,inplace=True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split("[")[0]))
Ans =df.head()
#Question 84
#년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
Ans = df[(df['Period'] >=2015) & (df['Dim1'] =='Both sexes')]
#Question 85
#84번 문제에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
Ans = Ans.pivot(index='Location', columns='Period', values='First Tooltip')
#Question 86
#Dim1에 따른 년도별 사망비율의 평균을 구하라
Ans = df.pivot_table(index='Dim1', columns='Period', values='First Tooltip',aggfunc='mean')


df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv')
Ans = df.head(3)
#Question 87
#데이터에서 한국 KOR 데이터만 추출하라
Ans = df[(df['Country']=='KOR')]
#Question 88
#한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
Ans = Ans.pivot_table(index='Year', columns='Medal',aggfunc='size', fill_value=0)
#Question 89
# 전체 데이터에서 sport종류에 따른 성별수를 구하여라
Ans = df.pivot_table(index='Sport',columns='Gender',aggfunc='size', fill_value=0)
#Question 90
#전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
Ans = df.pivot_table(index='Discipline', columns='Medal', aggfunc='size')

print(Ans)