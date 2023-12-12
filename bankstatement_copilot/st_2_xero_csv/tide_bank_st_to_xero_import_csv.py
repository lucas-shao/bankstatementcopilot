import pandas as pd


def process_st_csv(input_path: str, output_path: str):
    # 读取 CSV 文件
    df = pd.read_csv(
        input_path,
    )

    # 填充缺失的数据为0
    df["Paid in (£)"].fillna(0, inplace=True)
    df["Paid out (£)"].fillna(0, inplace=True)

    # 合并'In (£)'和'Out (£)'列到新的列'Amount'
    df["Amount"] = df["Paid in (£)"] - df["Paid out (£)"]

    # 去除'in'和'out'列
    df.drop(columns=["Paid in (£)", "Paid out (£)"], inplace=True)

    # 将 DataFrame 写入新的 CSV 文件
    df.to_csv(
        output_path,
        index=False,
    )
