import pandas as pd
import matplotlib.pyplot as plt

# 读取 Excel 文件
df = pd.read_excel("resourse/sorted_income_summary.xlsx", engine="openpyxl")

# 计算每个对手方的总金额占比
df_summary = df.groupby("Counterparty").agg({"Total Amount": "sum"})
df_summary["Percentage"] = (
    df_summary["Total Amount"] / df_summary["Total Amount"].sum() * 100
)

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(df_summary["Percentage"], labels=df_summary.index, autopct="%1.1f%%")
ax.set_title("Income by Counterparty")

plt.show()
