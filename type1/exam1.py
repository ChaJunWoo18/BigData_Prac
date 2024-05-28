import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)

#1 인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
top10_index = df['channelId'].value_counts().head(10).reset_index(drop=False)
answer = df[df['channelId'].isin(top10_index['channelId'])]['channelTitle'].unique()

#2 논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 likes 수보다 높은 동영상을 제작한 채널을 모두 출력하라
answer = df[df['dislikes'] > df['likes']]['channelTitle'].unique()

#3 채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
change = df[['channelId','channelTitle']].drop_duplicates()['channelId'].value_counts()
answer = change[change > 1]
answer = len(answer)

#4 일요일에 인기있었던 영상들 중 가장 많은 영상 종류(categoryId)는 무엇인가?
df['trending_date2'] = pd.to_datetime(df.trending_date2)
answer = df[df['trending_date2'].dt.day_name()=='Sunday']['categoryId'].value_counts().index[0]

#5 각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
group = df.groupby([df['trending_date2'].dt.day_name(),'categoryId'],as_index=False).size()
answer = group.pivot(index='categoryId', columns='trending_date2')

#6 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다. view_count대비 댓글수가 가장 높은 영상을 확인하라
# (view_count값이 0인 경우는 제외한다)
target = df[df['view_count']!=0]
target.loc[:, 'ratio'] = (target['comment_count']/target['view_count']).dropna()
answer = target.sort_values(by='ratio', ascending=False).iloc[0].title

#7 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다.viewcount대비 댓글수가 가장 낮은 영상을 확인하라
# (view_counts, ratio값이 0인경우는 제외한다.)
ratio = (df['comment_count']/df['view_count']).dropna().sort_values()
answer = df.iloc[ratio[ratio!=0].index[0]].title

#8 like 대비 dislike의 수가 가장 적은 영상은 무엇인가? (like, dislike 값이 0인경우는 제외한다)
target = df.loc[(df.likes!=0) & (df.dislikes!=0)]
idx = (target['dislikes']/target['likes']).sort_values().index[0]
answer = df.iloc[idx].title

#9 가장 많은 트렌드 영상을 제작한 채널의 이름은 무엇인가? (날짜기준, 중복포함)
answer = df.loc[df.channelId==df.channelId.value_counts().index[0]].channelTitle.unique()[0]

#10 20회(20일)이상 인기동영상 리스트에 포함된 동영상의 숫자는?
answer = (df[['title','channelId']].value_counts()>=20).sum()

channel =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv')
video =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv')

#11 각 데이터의 ‘ct’컬럼을 시간으로 인식할수 있게 datatype을 변경하고 video 데이터의 videoname의 각 value 마다 몇개의 데이터씩 가지고 있는지 확인하라
channel.ct = pd.to_datetime(channel.ct)
video.ct = pd.to_datetime(video.ct)
answer = (video.groupby(video.videoname).size()) # print(video.videoname.value_counts())

#12 수집된 각 video의 가장 최신화 된 날짜의 viewcnt값을 출력하라
answer = (video.sort_values(by=['videoname','ct'])).drop_duplicates('videoname',keep='last')[['viewcnt','videoname','ct']]

#13 channel 데이터중 2021-10-03일 이후 각 채널의 처음 기록 됐던 구독자 수(subcnt)를 출력하라
answer = channel[channel.ct>='2021-10-03'].sort_values('ct').drop_duplicates('channelname')[['subcnt','channelname']].reset_index(drop=True)

#14 각채널의 2021-10-03 03:00:00 ~ 2021-11-01 15:00:00 까지 구독자수 (subcnt) 의 증가량을 구하여라
start = channel[channel.ct.dt.strftime('%Y-%m-%d %H') == '2021-10-03 03']
end = channel[channel.ct.dt.strftime('%Y-%m-%d %H') == '2021-11-01 15']
start_df = start[['channelname','subcnt']].reset_index(drop=True)
end_df = end[['channelname','subcnt']].reset_index(drop=True)

start_df.columns = ['channelname','start_subcnt']
end_df.columns = ['channelname','end_subcnt']

tt = pd.merge(start_df, end_df)
tt['increase'] = tt['end_subcnt'] - tt['start_subcnt']
answer = (tt[['channelname','increase']])

#15 각 비디오는 10분 간격으로 구독자수, 좋아요, 싫어요수, 댓글수가 수집된것으로 알려졌다. 
# 공범 EP1의 비디오정보 데이터 중 수집 간격이 5분 이하, 20분이상인 데이터 구간( 해당 시점 전,후) 의 시각을 모두 출력하라
#print(video.columns)
import datetime # datetime.timedelta
ep_one = video.loc[video.videoname.str.contains('1')].sort_values('ct').reset_index(drop=True)

print(ep_one[
        (ep_one.ct.diff(1) >=datetime.timedelta(minutes=20)) | \
        (ep_one.ct.diff(1) <=datetime.timedelta(minutes=5))
      ])






#print(answer)