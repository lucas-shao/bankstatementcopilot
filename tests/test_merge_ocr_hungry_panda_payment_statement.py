import os
import asyncio

import pandas as pd

from bankstatement_copilot.http.bkp_client import (
    ocrBankStatement,
    ocrHungryPandaPaymentStatement,
)
from bankstatement_copilot.http.model.ocr_request import OcrRequest


# csv文件夹路径
directory = "/Users/shaoshuai.shao/Downloads/Hungry_Panda_20240605/csv/"

# 生成的csv文件路径
out_file_dir = directory + "result/"
out_file_path = out_file_dir + "result.csv"

# 自定义列名
column_names = [
    "Paltform",
    "StatementNumber",
    "Date Range",
    "Food Order Value",
    "Commission",
    "VAT",
    "Discount Merchant",
    "Delivery Fee Merchant",
    "Delivery Fee Customer",
    "Merchant other Income",
    "Adjustment",
    "Net Payment",
    "Food Order Value - V",
    "Commission - V",
    "VAT - V",
    "Discount Merchant - V",
    "Delivery Fee Merchant - V",
    "Delivery Fee Customer - V",
    "Merchant other Income - V",
    "Adjustment - V",
    "Net Payment - V",
    "Credit",
    "Total",
]


async def main():
    # 创建文件夹 out_file_dir
    if not os.path.exists(out_file_dir):
        os.makedirs(out_file_dir)

    # 创建一个空的DataFrame，并指定列名
    df = pd.DataFrame(columns=column_names)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为 csv 文件
        if filename.endswith(".csv"):
            # 帮我读取每个CSV文件的第二行数据
            statement = pd.read_csv(directory + filename)
            print(statement)

            # 然后将读取到的数据追加到df中
            df = pd.concat([df, statement])

    # 将 DataFrame 写入新的 CSV 文件
    df.to_csv(
        out_file_path,
        index=False,
    )

    print("Panda CSV file generated successfully! " + out_file_path)


asyncio.run(main())
