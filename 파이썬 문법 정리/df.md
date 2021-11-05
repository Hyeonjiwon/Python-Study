```python
## xlsx 파일 불러오기 
import pandas as pd
import openpyxl

df = pd.read_excel('파일명.xlsx', engine = 'openpyxl', sheet_name = 1)
df

## F- 로 시작하는 지점번호 행만 남겨두기
df_f = df1[df1['지점번호'].str.contains('F-')]

# 특정 칼럼을 기준으로 행을 정렬한 후 
# 각 그룹별 상위 N개의 행을 가져오기
# 규모별 건물 면적 순으로 상위 3개 행 선택하기 
df_sort_group_top3 = df.sort_values(by="건물면적",ascending=False).groupby("규모").head(3)
df_sort_group_top3.head(50)


```