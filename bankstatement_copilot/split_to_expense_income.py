import pandas as pd

# 读取 Excel 文件
df = pd.read_excel("resourse/bankstatement_mid_data_1.xlsx", engine="openpyxl")

# 创建支出项和收入项的 DataFrame
df_expenses = df[df["Column_2"] < 0]
df_income = df[df["Column_2"] > 0]

df_expenses_summary = df_expenses.groupby("Column_3").agg(
    {"Column_2": "sum", "Column_3": "count"}
)
df_income_summary = df_income.groupby("Column_3").agg(
    {"Column_2": "sum", "Column_3": "count"}
)

# 将 DataFrame 写入新的 Excel 文件
df_expenses_summary.to_excel(
    "resourse/expenses_summary.xlsx", index=True, engine="openpyxl"
)
df_income_summary.to_excel(
    "resourse/income_summary.xlsx", index=True, engine="openpyxl"
)
