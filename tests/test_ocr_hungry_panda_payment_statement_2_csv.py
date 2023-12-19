import os
import asyncio

import pandas as pd

from bankstatement_copilot.http.bkp_client import (
    ocrBankStatement,
    ocrHungryPandaPaymentStatement,
)
from bankstatement_copilot.http.model.ocr_request import OcrRequest

file_url_list = [
    "https://oss.xiaocichang.com/file/24805_2023.07.17-2023.07.23_1690337288510.pdf",
]

out_file_path = "/Users/shaoshuai.shao/Desktop/hungry_panda_payment_statement.csv"

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
    "Merchant other Income",
    "Adjustment",
    "Net Payment",
    "Food Order Value - V",
    "Commission - V",
    "VAT - V",
    "Discount Merchant - V",
    "Delivery Fee Merchant - V",
    "Merchant other Income - V",
    "Adjustment - V",
    "Net Payment - V",
    "Credit",
    "Total",
]


async def main():
    statements = []
    for statement_file_url in file_url_list:
        ocrRequest = OcrRequest()
        ocrRequest.secret_key = (
            "qI4dqCZaw0tkmwpMKrtAJ6NWabCsboPGb7wT1EUL4ohBaczIcdNac9su9NSOeGJuLH"
        )
        ocrRequest.file_path = statement_file_url
        res = await ocrHungryPandaPaymentStatement(ocrRequest)
        print(res)

        statements.append(res.data)

    print("statements")
    print(statements)

    if statements != None and len(statements) > 0:
        # 创建一个空的DataFrame，并指定列名
        df = pd.DataFrame(columns=column_names)

        for statement in statements:
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


asyncio.run(main())
