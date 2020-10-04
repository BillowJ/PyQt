from pyecharts.charts import Bar
import pandas as pd
import numpy as np
data = pd.read_csv('E:/Diplomat_Project/MyProject/pac/RunTo/DATA_2020_09_04.csv', encoding='gbk')
df = pd.DataFrame(data)
print(df)

print(df.loc[df['Place_Y'] == "仓山区"])
res = df.query('Place_Y == "仓山区"')
print(res)