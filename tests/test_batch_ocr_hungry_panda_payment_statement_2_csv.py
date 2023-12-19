import os
import asyncio

import pandas as pd

from bankstatement_copilot.http.bkp_client import (
    ocrBankStatement,
    ocrHungryPandaPaymentStatement,
)
from bankstatement_copilot.http.model.ocr_request import OcrRequest

# PDF的URL前缀
pdf_url_prefix = "https://oss.xiaocichang.com/file/hungry_panda_20231215/"

# PDF文件夹路径
directory = "/Users/shaoshuai.shao/Downloads/HP/"

# 已经处理完毕的PDF文件夹路径
processed_file_directory = directory + "processed/"

# 生成的csv文件路径
out_csv_path = directory + "csv/"

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
    # 遍历文件夹中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为 pdf 文件
        if filename.endswith(".pdf"):
            # 创建文件夹 out_csv_path
            if not os.path.exists(out_csv_path):
                os.makedirs(out_csv_path)

            # 创建文件夹 processed_file_directory
            if not os.path.exists(processed_file_directory):
                os.makedirs(processed_file_directory)

            statement_file_url = pdf_url_prefix + filename
            out_file_path = out_csv_path + filename.replace(".pdf", ".csv")

            print("statement_file_url: " + statement_file_url)
            print("out_file_path: " + out_file_path)

            ocrRequest = OcrRequest()
            ocrRequest.secret_key = (
                "qI4dqCZaw0tkmwpMKrtAJ6NWabCsboPGb7wT1EUL4ohBaczIcdNac9su9NSOeGJuLH"
            )
            ocrRequest.file_path = statement_file_url
            res = await ocrHungryPandaPaymentStatement(ocrRequest)
            statement = res.data
            print(statement)

            # 创建一个空的DataFrame，并指定列名
            df = pd.DataFrame(columns=column_names)

            # 创建一个新的临时DataFrame来保存当前行的数据
            temp_df = pd.DataFrame(
                [
                    {
                        "Paltform": "Hungry Panda",
                        "StatementNumber": statement.statementNumber,
                        "Date Range": statement.orderPeriod,
                        "Food Order Value": statement.foodOrderValueNormalAndRefundAmount,
                        "Commission": statement.commissionNormalAndRefundAmount,
                        "VAT": statement.vatNormalAndRefundAmount,
                        "Discount Merchant": statement.discountMerchantNormalAndRefundAmount,
                        "Delivery Fee Merchant": statement.deliveryFeeMerchantNormalAndRefundAmount,
                        "Delivery Fee Customer": statement.deliveryFeeCustomerNormalAndRefundAmount,
                        "Merchant other Income": statement.merchantOtherIncomeNormalAndRefundAmount,
                        "Adjustment": statement.adjustmentNormalAndRefundAmount,
                        "Net Payment": statement.netPaymentNormalAndRefundAmount,
                        "Food Order Value - V": statement.foodOrderValueVoucherAndRefundAmount,
                        "Commission - V": statement.commissionVoucherAndRefundAmount,
                        "VAT - V": statement.vatVoucherAndRefundAmount,
                        "Discount Merchant - V": statement.discountMerchantVoucherAndRefundAmount,
                        "Delivery Fee Merchant - V": statement.deliveryFeeMerchantVoucherAndRefundAmount,
                        "Delivery Fee Customer - V": statement.deliveryFeeCustomerVoucherAndRefundAmount,
                        "Merchant other Income - V": statement.merchantOtherIncomeVoucherAndRefundAmount,
                        "Adjustment - V": statement.adjustmentVoucherAndRefundAmount,
                        "Net Payment - V": statement.netPaymentVoucherAndRefundAmount,
                        "Credit": statement.creditAmount,
                        "Total": statement.totalPaymentAmount,
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

            print("Panda CSV file generated successfully! " + out_file_path)

            # 将已经处理完毕的PDF文件移动到processed文件夹
            os.rename(
                directory + filename,
                processed_file_directory + filename,
            )


asyncio.run(main())
