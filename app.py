import pandas as pd
import os
from bankstatement_copilot.extract_statement_info import extract_contact_name
from bankstatement_copilot.extract_contact_from_statement import (
    extract_statement_contact_from_column_to_column,
)


# df = pd.read_excel("resourse/vk_bankstatementline.xlsx", engine="openpyxl")

# # 选取第四列和第七列
# column_4 = df.iloc[:, 3]
# column_7 = df.iloc[:, 6]

# # 创建新的DataFrame
# bankstatement_mid_data_1 = pd.DataFrame()

# # 将选取的列作为新DataFrame的列插入
# bankstatement_mid_data_1["Column_1"] = column_4
# bankstatement_mid_data_1["Column_2"] = column_7
# bankstatement_mid_data_1["Column_3"] = ""


# # 将新DataFrame写入新的Excel文件
# bankstatement_mid_data_1_path = "resourse/bankstatement_mid_data_1.xlsx"
# bankstatement_mid_data_1.to_excel(
#     bankstatement_mid_data_1_path, index=False, engine="openpyxl"
# )

df = pd.read_excel("resourse/bankstatement_mid_data_1.xlsx", engine="openpyxl")
bankstatement_mid_data_1 = pd.DataFrame()

column_1 = df.iloc[:, 0]
column_2 = df.iloc[:, 1]
column_3 = df.iloc[:, 2]
bankstatement_mid_data_1["Column_1"] = column_1
bankstatement_mid_data_1["Column_2"] = column_2
bankstatement_mid_data_1["Column_3"] = column_3

num_rows = column_1.shape[0]

for i in range(900, num_rows, 50):
    start_index = i
    end_index = i + 50 - 1
    end_index = min(end_index, num_rows - 1)
    extract_statement_contact_from_column_to_column(
        bankstatement_mid_data_1,
        "resourse/bankstatement_mid_data_1.xlsx",
        "Column_1",
        start_index,
        end_index,
        "Column_3",
        start_index,
        end_index,
    )
