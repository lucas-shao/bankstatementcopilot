import pandas as pd

# 读取 Excel 文件
df_expenses_summary = pd.read_excel("resourse/expenses_summary.xlsx", engine="openpyxl")
df_income_summary = pd.read_excel("resourse/income_summary.xlsx", engine="openpyxl")

# 重命名列名
df_expenses_summary.columns = ["Counterparty", "Total Amount", "Number of Transactions"]
df_income_summary.columns = ["Counterparty", "Total Amount", "Number of Transactions"]

# 对汇总的数据按 'Total Amount' 从大到小排序
df_expenses_summary = df_expenses_summary.sort_values(by="Total Amount", ascending=True)
df_income_summary = df_income_summary.sort_values(by="Total Amount", ascending=False)

# 将 DataFrame 写入新的 Excel 文件
df_expenses_summary.to_excel(
    "resourse/sorted_expenses_summary.xlsx", index=False, engine="openpyxl"
)
df_income_summary.to_excel(
    "resourse/sorted_income_summary.xlsx", index=False, engine="openpyxl"
)
