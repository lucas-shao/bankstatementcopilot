import os
import asyncio

import pandas as pd

from bankstatement_copilot.http.bkp_client import ocrBankStatement
from bankstatement_copilot.http.model.ocr_request import OcrRequest

bank_statement_file_url_list = [
    "https://assets.pinvo.ai/assets/file/20240420/AEBPC-3.pdf",
]

out_file_path = "/Users/shaoshuai.shao/Desktop/AEBPC-3.csv"

# 自定义列名
column_names = ["Date", "Description", "Amount", "Balance"]


async def main():
    bankStatementLines = []
    for bank_statement_file_url in bank_statement_file_url_list:
        ocrRequest = OcrRequest()
        ocrRequest.secret_key = (
            "qI4dqCZaw0tkmwpMKrtAJ6NWabCsboPGb7wT1EUL4ohBaczIcdNac9su9NSOeGJuLH"
        )
        ocrRequest.file_path = bank_statement_file_url
        res = await ocrBankStatement(ocrRequest)
        print(res)

        bankStatementLines.extend(res.data.bankStatementLineList)

    if bankStatementLines == None or len(bankStatementLines) == 0:
        print("No bank statement lines found!")
        return

    if bankStatementLines != None and len(bankStatementLines) > 0:
        # 创建一个空的DataFrame，并指定列名
        df = pd.DataFrame(columns=column_names)

        for bankStatementLine in bankStatementLines:
            # 创建一个新的临时DataFrame来保存当前行的数据
            temp_df = pd.DataFrame(
                [
                    {
                        "Date": bankStatementLine.date,
                        "Description": bankStatementLine.description
                        + " . "
                        + bankStatementLine.transactionType,
                        "Amount": bankStatementLine.amount,
                        "Balance": bankStatementLine.balance,
                    }
                ]
            )

            # 使用concat方法合并DataFrame
            df = pd.concat([df, temp_df], ignore_index=True)

        # 将 DataFrame 写入新的 CSV 文件
        df.to_csv(
            out_file_path,
            index=False,
        )

        print("Xero CSV file generated successfully! " + out_file_path)


asyncio.run(main())
