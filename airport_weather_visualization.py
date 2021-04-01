import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

alldata = pd.read_csv('airport_weather_data.csv', encoding='cp949', index_col=0)

alldata['일시'] = pd.to_datetime(alldata['일시'])

alldata.head()

alldata.info()

alldata = alldata.set_index('일시')

alldata.describe()

alldata.isna().sum()

alldata = alldata.fillna(0)

alldata.info()

alldata.head()

alldata = alldata.drop(['최대풍속 나타난시각(hhmi)','최대순간풍속 나타난시각(hhmi)','최고기온시각(hhmi)','최저기온시각(hhmi)','1시간최다강수 시각(hhmi)','평균운량(1/8)'], axis=1)

alldata.head()

GMP = alldata.loc[alldata['지점명']=='김포공항',]

GMP.head()

ICN = alldata.loc[alldata['지점명']=='인천공항',]

ICN.head()

CJU = alldata.loc[alldata['지점명']=='제주공항',]

CJU.head()





plt.figure(figsize=(25,15))
plt.plot(GMP['평균풍속(KT)'])
plt.title('김포 공항 일별 평균풍속')
plt.xlabel('일자')
plt.ylabel('평균 풍속')
plt.show()

plt.figure(figsize=(25,15))
plt.plot(GMP['평균풍속(KT)'],label = '평균풍속')
plt.plot(GMP['최대풍속(KT)'], label = '최대풍속')
plt.title('김포 공항 일별 평균 및 최대 풍속')
plt.xlabel('일자')
plt.ylabel('풍속')
plt.legend()
plt.show()



plt.figure(figsize=(25,15))

plt.subplot(1,2,1)
plt.hist(data = GMP, x= '최대풍속 풍향(deg)',rwidth = 0.5,label = '최대 풍속 풍향', bins =40)
plt.title('김포 공항 일별 최대풍속 풍향 ')
plt.xlabel('풍향')
plt.ylabel('빈도수')
plt.legend()
plt.subplot(1,2,2)
plt.hist(data =GMP, x ='최대순간풍속 풍향(deg)', rwidth = 0.5,label = '최대 순간 풍속 풍향', bins=40, color='r')
plt.title('김포 공항 일별최대 순간 풍속 풍향(gust)')
plt.xlabel('풍향')
plt.ylabel('빈도수')
plt.legend()
plt.show()

#RWY15보다 RWY33나 34를 더 주로 사용할것이란것 볼 수 있다.

plt.figure(figsize=(25,15))
plt.plot(GMP['최저기온(°C)'],label = '최저기온')
plt.plot(GMP['최고기온(°C)'], label = '최고기온',color = 'r')
plt.title('김포 공항 일별 기온')
plt.xlabel('일자')
plt.ylabel('기온')
plt.legend()
plt.show()

sns.pairplot(GMP)

plt.figure(figsize=(12,12))
plt.scatter(data=GMP,x='평균상대습도(%)',y='평균해면기압(hPa)')
plt.title('기압과 습도의 상관관계')
plt.xlabel('평균상대습도')
plt.ylabel('평균해면기압')
plt.show()

# 기압이 낮을수록 습도가 낮다(저기압에 습도가 높다..)



pivoted_alldata = pd.pivot_table(alldata, index = ['지점명'])

pivoted_alldata