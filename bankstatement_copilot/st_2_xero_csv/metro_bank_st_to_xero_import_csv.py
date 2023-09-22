import pandas as pd


def process_st_csv(input_path: str, output_path: str):
    # 读取 CSV 文件
    df = pd.read_csv(
        input_path,
    )

    # 将'out'列的值变为负数
    df["Out"] = df["Out"].apply(lambda x: -x)

    # 填充缺失的数据为0
    df["In"].fillna(0, inplace=True)
    df["Out"].fillna(0, inplace=True)

    # 合并'in'和'out'列到新的列'Amount'
    df["Amount"] = df["In"] + df["Out"]

    # 去除'in'和'out'列
    df.drop(columns=["In", "Out"], inplace=True)

    # 将 DataFrame 写入新的 CSV 文件
    df.to_csv(
        output_path,
        index=False,
    )
