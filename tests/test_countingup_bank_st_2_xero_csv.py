import os
from bankstatement_copilot.st_2_xero_csv.countingup_bank_st_to_xero_import_csv import (
    process_st_csv,
)

# 文件夹路径
directory = "/Users/shaoshuai.shao/Downloads/Countingup-statement/"

# 遍历文件夹中的所有文件
for filename in os.listdir(directory):
    # 检查文件是否为 CSV 文件
    if filename.endswith(".csv"):
        inputpath = os.path.join(directory, filename)
        outputpath = os.path.join(directory, "NEW_" + filename)
        process_st_csv(inputpath, outputpath)
