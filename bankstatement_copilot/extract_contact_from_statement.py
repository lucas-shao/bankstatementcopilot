import pandas as pd
from pandas import DataFrame
from bankstatement_copilot.extract_statement_info import extract_contact_name


def extract_statement_contact_from_column_to_column(
    data_frame: DataFrame,
    data_frame_path: str,
    source_column: str,
    from_source_line_id: int,
    to_source_line_id: int,
    target_column: str,
    from_target_line_id: int,
    to_target_line_id: int,
):
    # 读取源Column数据
    source_column_data = data_frame.loc[
        from_source_line_id:to_source_line_id, source_column
    ].tolist()

    # 处理源Column数据生成目标数据
    target_column_data = extract_contact_name(source_column_data)

    # 将目标数据赋值到目标Column
    data_frame.loc[
        from_target_line_id:to_target_line_id, target_column
    ] = target_column_data

    # 将新DataFrame写入新的Excel文件
    data_frame.to_excel(data_frame_path, index=False, engine="openpyxl")
