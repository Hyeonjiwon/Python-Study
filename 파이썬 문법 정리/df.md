```python
# xlsx 파일 불러오기 
import pandas as pd
import openpyxl

df = pd.read_excel('파일명.xlsx', engine = 'openpyxl', sheet_name = 1)

# 특정 행만 불러오기 
df = pd.read_excel('파일명.xlsx', engine = 'openpyxl', usecols=[11, 12])

# 유일한 값 찾기
df['규모'].unique()

# F- 로 시작하는 지점번호 행만 남겨두기
df_f = df1[df1['지점번호'].str.contains('F-')]

# 특정 문자와 일치하는 행 추출하기 
df[df.도서관명 == '도서관']
df[df["도서관명"] == '도서관']

# 특정 문자열을 포함하는 행 추출하기 
ddf = ddf[ddf['등록일자'].str.contains('2020') | ddf['등록일자'].str.contains('2021')]

# 문자열을 나누고 새로운 열 만들기
new_lib_list['주소1'] = new_lib_list.정보나루_주소.str.split(' ').str[0]

# 특정문자 기준으로 문자열 나누고 새로운 열 추가
ddf['년'] = ddf.등록일자.str.split('-').str[0]
ddf['월'] = ddf.등록일자.str.split('-').str[1]
ddf['일'] = ddf.등록일자.str.split('-').str[2]

# 특정 칼럼을 기준으로 행을 정렬한 후 
# 각 그룹별 상위 N개의 행을 가져오기
# 규모별 건물 면적 순으로 상위 3개 행 선택하기 
df_sort_group_top3 = df.sort_values(by="건물면적",ascending=False).groupby("규모").head(3)
df_sort_group_top3.head(50)

# 열 순서 변경 1
new_df = ddf[['등록일자', '년', '월', '일', '대출건수']]

# 열 순서 변경 2
col1 = flt_df.columns[:11].to_list()
col2 = flt_df.columns[-1:].to_list()
col3 = flt_df.columns[12:-1].to_list()
new_col = col1 + col2 + col3
new_df = flt_df[new_col]

# 월별 대출 건수
grouped_df = ddf.groupby(['년', '월']).sum()


```