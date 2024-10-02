'''
soruce : https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter01/Chapter%201%20pandas%20Foundations%20part%201.ipynb
date : 24.10.01.
'''
import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

employee,color,index,columns,comp1,comp2,rows,cols,years,budget,top10_roll=None


# pd options setting
pd.set_option('max_columns', 8, 'max_rows', 10)

# dataframe components
df = pd.DataFrame()
df.columns
df.index
df.values

# check data types
df.dtypes
df.get_dtype_counts() # 데이터 타입이 종류별로 몇개인지 알려줌

# get serires from df, display it df format
sr = df['col1']
sr.to_frame().head() # series 를 dataframe 양식으로 출력함

# display format
pd.set_option('max_ros', 8)
sr.value_counts()

sr.value_counts(normalize=True) # 갯수를 정규화 해서 나타냄

# display format
pd.options.display.max_rows = 6

# change column type and calculate
sr.astype(int).mod(5)
sr.fillna(0).astype(int).head()

# set dataframe index title
df2 = df.set_index('movie_title')
pd.read_csv('', index_col='movie_title') # set_index 대신에 파일을 불러올 때 설정 가능
df2.reset_index()

# list index, columns name
index_list = index.to_list()
column_list = columns.to_list()

# find column position
sr_index = df.columns.get_loc('col_name') + 1 # 컬럼 이름으로 컬럼 위치 찾기. 인덱싱을 위해 1 더함
df.insert(sr_index, 'add_col', df.a-df.b)

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter02/Chapter%202%20pandas%20Foundations%20part%202.ipynb
'''
# format setting
pd.options.display.max_columns = 40

# dataframe 에서 필요한 컬럼 뽑기
df_2 = df[['col1','col2']] # 컬럼으로 데이터프레임을 뽑을 때는 대괄호 [[]] 2개를 써야 한다

df.get_dtype_counts() # 데이터프레임에서 각 데이터 타입 별 컬럼 갯수 확인

# 컬럼을 조건 별로 뽑기
df.select_dtypes(include=['int'])       # 컬럼의 데이터 타입이 int 인 경우만 뽑기
df.select_dtypes(include=['number'])    # 컬럼이 숫자인 경우 뽑기, int, float 고름
df.filter(like=['facebook'])            # like 를 사용하여 컬럼에 해당 문자를 포함한 경우 뽑기
df.filter(regex='\d')                   # regex 사용
df.filter(items=['col1', 'ddol1'])

df.describe()
df.describe(percentile=[0.01,0.5,0.99])

# comparing
compare_res = comp1 == comp2

# pandas testing
from pandas.testing import assert_frame_equal # type: ignore
assert_frame_equal(df, df)

# 데이터프레임의 값 전체에 비교를 해서 true/false 확인하기
df.eq(.01)

# dataframe operation direction
df.count(axis=0)            # row direction, 밑으로 더해서 행 갯수만큼 나옴
df.count(axis='index')
df.count(axis='columns')    # column index, 가로로 더해서 컬럼 수 만큼 나옴

# 누적으로 더하기, cumsum
df_cumsum = df.cumsum(axis=1)

# sorting
df.sort_values('col1', ascending=False)

# index 를 지정해서 dataframe 불러오기
pd.read_csv('', index_col='col_index_name')

# dataframe 에서 해당 row 선택하기
df.loc['row1','row2']       ## 이렇게 row 를 선택하고, columns 은 다르게 선택함(loc 없이)

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter03/Chapter%203%20Beginning%20Data%20Analysis.ipynb
'''

pd.options.display.max_columns = 50

# display 행/렬을 바꿔서 보기 쉽게 하기
with pd.option_context('display.max_rows', 8):
    display(df.describe(include=[np.number]).T) # type: ignore

# number 가 아닌 것만 보기
df.describe(include=['np.object','pad.Categorical']).T

df.describe(inlcude=[np.number], percentile=[.01,.05,.10])

# reducing memroy by changing data types
df['col1'] = df['col2'].astype(np.int8)

# memory usage 확인하기
df['col1'].memory_usage(deep=True)

# selecting the smallest of the largest
df.nlargest(100,'col1')
df.nlargest(100,'col1').nsmallest(5,'col2')
df.sort_values(['col1','col2','col3'], ascending=[False,False,True])
df.drop_duplicated(subset=['col1','col2'])
df.sort_values('col1', ascending=False).head(10).sort_values('col2').head()

# calculating a trailing stop order price
import pandas_datareader as pdr # type: ignore
tsla = pdr.DataReader('tsla', data_source='google', start='2017-1-1')
tsla_close = tsla['Close']
tsla_cummax = tsla_close.cummax()

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter04/Chapter%204%20Selecting%20Subsets%20of%20Data.ipynb
'''
# selecting serires data
sr.iloc[3]          # 하나만 선택할 때는 대괄호 1개
sr.iloc[[10,20,30]] # 두개 이상 선택할 때는 대괄호 2개 사용해야 함

# index 로도 선택할 수 있음
sr.loc['a univ']

# random choice
np.random.seed(1)
labels = list(np.random.choice(sr.index, 5))    # sr.index 에서 랜덤으로 5개 선택함
sr.loc(labels)      # 이렇게 해서 랜덤한 인덱스에 해당하는 값을 선택
sr.loc['a univ':10] # 'a univ 에서부터 10개 전까지 선택

# 인덱스로 선택해 보자
sr.iloc[3]

# dataframe 에서 행/열 선택하기
df.iloc[[20,30,14]] # datafrme 에서 선택하려면 대괄호 2개를 사용해야 함
# 숫자로 지정하기 전에 선택할 항목을 미리 변수에 저장할 수 있음
labels=['a univ','b univ','c univ']
df.loc[labels]
df.iloc[20:30]
start = 'a univ'
end = 'e univ'
df.loc[start:end]   # 시작과 끝을 모두 변수로 저장한 다음에 할당

# 해당 항목의 인덱스만 추출 해보자
df.iloc[[20,30,40]].index.to_list()

# 행과 열을 동시에 가져오기
df.iloc[:3,:5]
df.iloc[:'d univ', 2:6]
df.loc[rows, cols]

# integers, labels 를 사용하여 컬럼 선택하기
col_start = df.columns.get_loc['univ AA']
col_end = df.columns.get_loc['univ DD'] + 1
col_start, col_end

df.iloc[:5, col_start:col_end]

row_start = df.index[4]
row_end = df.index[10]

# speeding up scalar selection, at 을 사용한다
df.loc['univ a']
df.at['univ a']

# 실행 시간 구하기, timeit
# %timeit df.loc['univ a']
# %timeit df.at['univ a']

# %timeit df.iloc[row_num,col_num]
# %timeit df.iat[row_num,col_num]

state = df['univ a']
state.iat[100]
state.at['univ a']

# 행열 선택하려면 두번째 방식으로 해야 함
df[:10, ['CITY','LOC']] # X
df_index = df.index[:10]
df.loc[df_index,['CITY','LOC']] # O

# 정렬해서 로지컬로 선택하기
df = df.sort_index()
pd.option.display.max_rows = 6
df.loc['Sp':'Su']

df = df.sort_index(ascending=False)
df.index.is_monotonic_decreasing
df.loc['E':'B']

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter05/Chapter%205%20Boolean%20Indexing.ipynb
'''

df = df['col1'] > 20
df['col1'].dropna().gt(120).mean() # col1 이 120 보다 크면 1, 작으면 0 으로 했을 때 평균값

# mutiple boolean conditions
criteria1 = df.col1 > 8
criteria2 = df.col2 < 20
criteria3 = (df.col3 < 2000) | (df.col4 > 20)
criteria_final = criteria1 & criteria2 & criteria3

df_filter = df.loc[criteria_final, ['col1','col5']]

# index selection
df[df['col1'] == 'AA']
df.loc['AA']

state = ['AA','BB','CC']
df[df['STATE'].isin(state)]
df.loc[state]

# unique
df.index.is_unique

df.index = df['CITY'] + ', ' + df['COUNTRY']
df = df.sort_index()

# gain perspective
df_summary = df.describe(percentile=[.1,.9])
upper_10 = df_summary.loc['90%']
lower_10 = df_summary.loc['10%']
criteria = (df<lower_10) | (df>upper_10)
df_topbottom = df[criteria]

# plot
df.plot(color='b', figsize=(10,4))
df_topbottom.plot(marker='o', style=' ', ms=4, color='r')
xmin = criteria.index[0]
xmax = criteria.index[-1]
plt.hlines(y=[lower_10,upper_10], xmin=xmin, xmax=xmax, color='r')
plt.fill_between(criteria.index, lower_10, df.values)
plt.fill_between(criteria.index, lower_10, df.values, where=df<lower_10, color='y')
plt.fill_between(criteria.index, upper_10, df.values, where=df>upper_10, color='y')

# improving readability with the query method
query_string = ""
df_filtered = df.query(query_string)

# mask
df_filtered = df.mask(criteria).dropna(how='all')

df_loc = df.loc[criteria]

df.iloc[criteria]           # X
df.iloc[criteria.values]    # O

criteria_col = df.dtypes == np.int64
df.loc[:, criteria_col]
df.iloc[:, criteria_col.values]

cols = ['col1','col2','col3']
col_index = [df.columns.get_loc(col) for col in cols]

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter06/Chapter%206%20Index%20Alignment.ipynb
'''
# appending columns
df_salary = df.sort_values(['col1','col2'], ascending=[True,False])
max_df_salary = df_salary.drop_duplicates(subset='col3')

random_df = df.sample(n=10).set_index()

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter07/Chapter%2007%20Grouping%20for%20Aggregation%2C%20Filtration%20and%20Transformation.ipynb
'''
# groupby
df.groupby('col1')['col2'].agg('mean')
df.groupby('co1').agg({'col2':'mean'})
df.groupby('col1')['col2'].agg(np.mean)
df.groupby('col1')['col2'].mean()

df.groupby(['col1','col2'])['col3'].agg('sum')
df.groupby(['col1','col2'])['col3','col3'].agg(['sum','mean'])
df.groupby(['col1','col2']).agg({'col3':['sum','mean','size'], 'col4':['mean','var']})

# removing the multiindex after grouping
df.groupby(['col1','col2']).agg({'col3':['sum','mean'], 'col4':['min','max']}).astype(int)
lv0 = df.columns.get_level_value(0) # column name 에서 level 0 의 이름 확인
lv1 = df.columns.get_level_value(1) # column name 에서 level 1 의 이름 확인
df.columns = lv0 + '_' + lv1
df.reset_index()                    # 컬럼명을 재정의 한 후 인덱스 원복
 
df.groupby(['col1'], as_index=False)['col2'].agg('mean').round(0)
df.groupby(['col1'], as_index=False, sort=False)['col2'].agg('mean').round(0)

# customizing
def max_deviations(s):
    std_score = (s - s.mean()) / s.std()
    return std_score.abs().max()
max_deviations.__name__ = 'Max Deviation'
df.groupby('col1')['col2','col3','col4'].agg(max_deviation).round(1).head()
df.groupyby(['col1','col2'])['col3','col4'].agg([max_deviations,'mean','std']).round(1)

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter08/Chapter%2008%20Restructuring%20Data%20into%20Tidy%20Form.ipynb
'''
# stack
df.stack()      # df 에서 x축->y축->값으로 데이터프레임 모양을 변경함. 데이터프레임은 아님

# reset_index 하면 데이터프레임 형태로 변환
df1 = df.stack().reset_index() # 데이터프레임 형태로 변환
df1.columns = ['col1','col2','col3']     # 컬럼 이름 설정

df.stack().rename_axis(['col1','col2']) # stack 할 때 name 설정
df.stack().rename_axis(['col1','col2']).reset_index(name='col3')    # stack 전 값이 들어가는 컬럼에도 이름 설정

# index 를 미리 설정
df.set_index('col1').stack()

# melt 를 사용하여 깔끔하게 하기
df.melt(id_var=['col1'], value_var=['cola','colb','colc']) # 첫행은 id_var, 두번쨰행은 value_var 로 설정함

'''
https://github.com/AcornPublishing/pandas-cookbook/blob/main/Chapter11/Chapter%2011%20Visualization%20with%20Matplotlib%2C%20Pandas%20and%20Seaborn.ipynb
'''
plt.title('Line Plot')
# subtitle 추가하기
plt.suptitle('Figure Title', size=20, y=1.03) 

fig, ax = plt.subplots(figsize=(15,3))
type(fig) # matplotlib.figure.Figure
type(ax) # matplotlib.axes._subplots.AxesSubplot
fig.set_size_inches(14, 4) # fig 사이즈 설정
fig.axes # [<matplotlib.axes._subplots.AxesSubplot at 0x1134202b0>]
fig.set_facecolor('.9')
ax.set_facecolor('.7')
spines = ax.spines # OrderedDict([('left', <matplotlib.spines.Spine at 0x113414da0>),
            #  ('right', <matplotlib.spines.Spine at 0x113434fd0>),
            #  ('bottom', <matplotlib.spines.Spine at 0x113434d30>),
            #  ('top', <matplotlib.spines.Spine at 0x113434e48>)])

fig2, ax_array = plt.subplots(2, 1, figsize=(14,6), sharex=True)
ax1 = ax_array[0]
ax2 = ax_array[1]
ax1.plot(years, budget, linestyle='--', linewidth=3, color='.2', label='All Movies')
ax2.plot(years, top10_roll.values, color='.2', label='Top 10 Movies')

# plotting basics with pandas
df.plot(kind='bar', color=color, figsize=(16,4))
df.plot(kind='kde', color=color, figsize=(16,4))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16,4))
fig.suptitle('Two Variable Plots', size=20, y=1.02)
# line graph
df.plot(kind='line', color=color, ax=ax1, title='Line plot')
# scatter graph
df.plot(x='Apples', y='Oranges', kind='scatter', color=color, ax=ax2, title='Scatterplot')
# bar graph
df.plot(kind='bar', color=color, ax=ax3, title='Bar plot')

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16,4))
fig.suptitle('One Variable Plots', size=20, y=1.02)
# kde
df.plot(kind='kde', color=color, ax=ax1, title='KDE plot')
# box
df.plot(kind='box', ax=ax2, title='Boxplot')
# hist
df.plot(kind='hist', color=color, ax=ax3, title='Histogram')

# subplot (2,3)
fig, ax_array = plt.subplots(2, 3, figsize=(18,8))
(ax1, ax2, ax3), (ax4, ax5, ax6) = ax_array

# seaborn
sns.countplot(y='DEPARTMENT', data=employee)
employee['DEPARTMENT'].value_counts().plot('barh')
ax = sns.barplot(x='RACE', y='BASE_SALARY', data=employee)
ax.figure.set_size_inches(16, 4)
ax = sns.barplot(x='RACE', y='BASE_SALARY', hue='GENDER', data=employee, palette='Greys')
ax.figure.set_size_inches(16,4)

