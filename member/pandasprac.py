import pandas as pd
from django.shortcuts import render
from .forms import SigninForm, SignupForm #이전에 만든 form 클래스를 선언해주고
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User #User 모델을 사용하기위해 선언해준다.

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
a = s1 + s2
print(a)

s3 = pd.Series([1,2,3,4])
s4 = pd.Series([10,20,30,40,50])
b = s3 + s4
print(b)

c = s4 * s3
print(c)

d = s4 / s3


abc = table_data1 ={'A':[1,2,3,4,5],
            'B':[10,20,30,40,50],
            'C':[100,200,300,400,500] }


import pandas as pd
import numpy as np

 

KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4169, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

 

df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)
df_KTX
