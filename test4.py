import pandas as pd
### Time

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')
#Ans = df.info()

#65 Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df['Yr_Mo_Dy'] = pd.to_datetime(df.Yr_Mo_Dy)
Ans = df['Yr_Mo_Dy']
# 66 Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
Ans = df['Yr_Mo_Dy'].dt.year.unique()
#Question 67
#Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
def changer(x):
    #import datetime
    year = x.year-100 if x.year>=2061 else x.year
    #return pd.to_datetime(datetime.date(year, x.month, x.day))
    return pd.Timestamp(year, x.month, x.day)
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(changer)
Ans = df['Yr_Mo_Dy']
#Question 68
#년도별 각 컬럼의 평균값을 구하여라
Ans = df.groupby(df['Yr_Mo_Dy'].dt.year).mean()
# Question 69
# weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
df['weekday'] = df['Yr_Mo_Dy'].dt.weekday
Ans = df['weekday'].to_frame()
# Question 70
# weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
df['WeekCheck'] = df['weekday'].map(lambda x:1 if x==5 or x==6 else 0) #if x in [5,6]
Ans = df['WeekCheck']
# Question 71
# 년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
Ans = df.groupby(df.Yr_Mo_Dy.dt.month).mean().head()
# Question 72
# 모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
df= df.ffill().bfill()
Ans = df.isnull().sum()
# Question 73
# 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
# Series.dt.to_period(freq)
# to_period 메소드는 Pandas의 Series 또는 DataFrame에서 datetime 객체를 기간(period) 객체로 변환하는 데 사용됩니다.
# 기간은 특정 날짜가 아닌 일정한 시간 간격을 나타내며, 연, 월, 분기, 일 등 다양한 단위로 지정할 수 있습니다.
# 'A': 연도 (Annual)
# 'Q': 분기 (Quarter)
# 'M': 월 (Month)
# 'W': 주 (Week)
# 'D': 일 (Day)
#.dt.strftime('%Y-%m')
Ans = df.groupby(df['Yr_Mo_Dy'].dt.strftime('%Y-%m')).mean()
Ans = df.groupby(df.Yr_Mo_Dy.dt.to_period('M')).mean()
#print(help(df.Yr_Mo_Dy.dt.to_period()))
# Question 74
# RPT 컬럼의 값을 일자별 기준으로 1차차분하라
Ans = df.RPT.diff()
# Question 75
# RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라 ***
Ans= df[['RPT','VAL']].rolling(7).mean()
#####################################################################################
df =pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv')
#76
#년-월-일:시 컬럼을 pandas에서 인식할 수 있는 datetime 형태로 변경하라. 서울시의 제공데이터의 경우 0시가 24시로 표현된다
def change_date(x):
    #2021-05-15:15
    import datetime
    date = x.split(":")[0]
    hour = x.split(":")[1]
    if hour == '24':
        hour = '00:00:00'
        FinalDate = pd.to_datetime(date+" "+hour)+datetime.timedelta(days=1)#하루 증가
    else:
        hour = hour+":00:00"
        FinalDate = pd.to_datetime(date +" "+hour)
    return FinalDate
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change_date)
Ans = df.head(3)
# Question 77
# 일자별 영어요일 이름을 dayName 컬럼에 저장하라
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
Ans = df['dayName']
# Question 78
# 일자별 각 PM10등급의 빈도수를 파악하라
df['date'] = df['(년-월-일:시)'].dt.date
Ans = df.groupby(['date','PM10등급'],as_index=False).size()
Ans = Ans.pivot(index='date',columns='PM10등급',values='size').fillna(0)
# Question 79
# 시간이 연속적으로 존재하며 결측치가 없는지 확인하라
check = len(df['(년-월-일:시)'].diff().unique())
if check==2:
    Ans = True
else:
    Ans =False
    
# Question 80
# 오전 10시와 오후 10시(22시)의 PM10의 평균값을 각각 구하여라
#print(df['(년-월-일:시)'].dt.hour.iloc[[10,22]])
Ans = df.groupby(df['(년-월-일:시)'].dt.hour)['PM10'].mean().loc[[10,22]]

# Question 81
# 날짜 컬럼을 index로 만들어라
df.set_index('(년-월-일:시)', inplace=True) #drop=True 는 기본값
Ans = df.head()

# Question 82
# 데이터를 주단위로 뽑아서 최소,최대 평균, 표준표차를 구하여라
Ans = df.info()
Ans = df.select_dtypes(exclude='object').resample('W').agg(['min','max','mean','std'])

print(Ans)  