import pandas as pd
import numpy as np
import re
source=r'C:\DevOps\FirstProject\Tuanizback\PJ01-tuanizback\Learn\Hangul\Youth\Filter\Youth-01-pandas-netflix-dual-sub.md'
df = pd.read_csv(source,encoding = 'utf-8',on_bad_lines='skip',sep = ';', header = None)
result = df.head(20)
# print("First 10 rows of the DataFrame:")
# print(result)
# print(len(df.axes[0]) )
# print(len(df.axes[1]))
df = pd.DataFrame(df.values.reshape(-1, 2), 
                   columns=['number', 'text'])
# print(df.head(20))
df['bolded']=''
pattern = r'(\*\*|__)(.*?)\1'
for ind in df.index:
    # print(df['text'][ind].findall('(\*\*|__)(.*?)\1'))
     #^.*(word1|word2|word3).*\n?
    line=df['text'][ind]
    df['bolded'][ind] = re.findall(pattern,line)
    # print(df['number'][ind], df['text'][ind],df['bolded'][ind])
    print(df['bolded'][ind])
    for i in df['bolded'][ind]:
        print(i)
    if ind > 20:
        break