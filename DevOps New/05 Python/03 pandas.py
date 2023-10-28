import pandas as pd
source=r'C:\DevOps\FirstProject\Tuanizback\PJ01-tuanizback\Learn\Hangul\Dream Project\Python subtitle\Dream-main-sub.csv'
df = pd.read_csv(source,encoding = 'utf-8',on_bad_lines='skip',sep = ';', header = None)
result = df.head(20)
print("First 10 rows of the DataFrame:")
print(result)
print(len(df.axes[0]) )
print(len(df.axes[1]))