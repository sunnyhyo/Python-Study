# -*- coding: utf-8 -*-

# =============================================================================
# BIZ & AI lab study 1-2. pandas
# =============================================================================


import pandas as pd
import numpy as np

# =============================================================================
# dictionary
# =============================================================================
ex_data = {'a':4.2,
        'b':3.8,
        'c':None,
        'd':4.0}
type(ex_data)
ex_data
ex_data['a']

ex_data.keys()
ex_data.values()
ex_data.items()
list(ex_data.items())

data_dict = {'name':['A', 'B', 'C', 'D'],
        'age':[24, 21, 22, 24],
        'height':[182, 164, 166, 175],
        'weight':[80, 54, 56, 75]}
data_dict

# =============================================================================
# Series 생성
# =============================================================================
obj = pd.Series(ex_data)
type(obj)
obj

obj_2 = pd.Series([4.2, 3.8, None, 4.0], index=['A', 'B', 'C', 'D'])
obj_2

obj_2['D']

obj.keys()
obj.values

# =============================================================================
# DataFrame 생성
# =============================================================================
data_dict
ex_df = pd.DataFrame(data_dict)
type(ex_df)
ex_df

ex_df.shape

ex_df.head(2)
ex_df.tail(2)

ex_df.keys()
ex_df.values

df = pd.DataFrame(data_dict, columns=['age', 'height', 'weight'], index=data_dict['name'])
df

df.T

df.columns = ['AGE', 'HEIGHT', 'WEIGHT']
df

df.index = ['a', 'b', 'c', 'd']
df

# =============================================================================
# DataFrame slicing
# =============================================================================
df.AGE
df['AGE']
df[['AGE', 'HEIGHT']]

df.ix['a']
df.ix[['a','b']]

# =============================================================================
# DataFrame 수정&추가&삭제
# =============================================================================
df = df.set_value('a', 'AGE', 20)
df

df.loc['z'] = None
df

df['test'] = 1
df

df['test_1'] = [None, 1, 2, 3, 4]
df

df['test_1'] = np.arange(df.shape[0])
df

df['gpa'] = obj
df


del df['test']
df

df = df.drop('test_1', axis=1)
df

df = df.drop('z', axis=0)
df

# =============================================================================
# # DataFrame 결합
# =============================================================================
data_dict_1 = {'name':['X', 'Y'],
        'AGE':[22, 22],
        'HEIGHT':[180, 170],
        'WEIGHT':[70,50]}

df_1 = pd.DataFrame(data_dict_1, columns=['AGE', 'HEIGHT', 'WEIGHT'], index=data_dict_1['name'])
df_1

df_con = pd.concat([df, df_1], axis=0, join='outer')
df_con


data_dict_2 = {'name':['X', 'Y'],
        'GENDER':['M', 'F']}

df_2 = pd.DataFrame(data_dict_2, columns=['GENDER'], index=data_dict_2['name'])
df_2

df_con = pd.concat([df_con, df_2], axis=1, join='outer')
df_con

# =============================================================================
# DataFrame 결측치
# =============================================================================
df
pd.isnull(df)
pd.notnull(df)

pd.isnull(df['gpa'])
pd.isnull(df.ix['c'])

# =============================================================================
# pandas 파일 로드
# =============================================================================
read_file_path = 'F:\\ibis_ywy\\B.I\\BIZ_file\\BIZ&AI\\4기\\BIZ_강의\\'
read_file_name = '1_ex_hw_2_label_data.csv'

import os
os.chdir(read_file_path)

#data_df = pd.read_csv(read_file_path+read_file_name)
data_df = pd.read_csv(read_file_name, engine='python')
data_df.shape
data_df.head()

# =============================================================================
# pandas 데이터 다루기
# =============================================================================
df

df.replace(np.nan, 0)
df
df.replace(np.nan, 0, inplace=True)
df

data_df['AGE'].min()
np.min(data_df['AGE'])
np.max(data_df['AGE'])
np.mean(data_df['AGE'])
np.median(data_df['AGE'])

data_df[data_df['AGE_CLASS']==20]
data_df[data_df['AGE_CLASS']==20]['AGE']
np.mean(data_df[data_df['AGE_CLASS']==20]['AGE'])
data_df[data_df['AGE_CLASS']==20]['AGE'].count()

data_df[data_df['AGE_CLASS']==20][data_df['GENDER']=='M']


data_df.groupby(['AGE_CLASS'])['AGE'].agg(np.mean)
data_df.groupby(['AGE_CLASS'])['AGE'].agg([np.min, np.max, np.mean, np.std])
data_df.groupby(['AGE_CLASS', 'GENDER'])['AGE'].agg(np.mean)


# =============================================================================
# pandas 파일 저장
# =============================================================================
write_file_path = read_file_path
write_file_name = '1_ex_data_20s.csv'
write_file_name_2 = '1_ex_data_20s.xlsx'

save_df = data_df[data_df['AGE_CLASS']==20]
save_df.head()

save_df.to_csv(write_file_path+write_file_name, header=True, index=False)
save_df.to_excel(write_file_path+write_file_name_2, header=True, index=False)
