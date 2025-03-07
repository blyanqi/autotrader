import pandas as pd
from io import StringIO
# 示例数据
data = """
时间,成交价,手数,买卖盘性质
09:15:03,12.38,23,中性盘
09:15:06,12.38,767,中性盘
09:15:09,12.38,1063,中性盘
09:15:12,12.38,1470,中性盘
"""

df = pd.read_csv(StringIO(data))

# 筛选时间在 09:15 的所有交易
filtered_df = df[df['时间'].str.startswith('09:15')]
# 找到第一笔交易
first_trade = filtered_df.iloc[0] if not filtered_df.empty else None

# 输出结果
if first_trade is not None:
    print("09:15 的第一笔交易：")
    print(first_trade)
else:
    print("在 09:15 没有交易记录。")
