import pandas as pd
from bankstatement_copilot.langchain.langchain_chat import LangchainAgent

chat_template = """
帮我在英国查找关于我的对手方「{0}」的信息，可以从对应的官方网站，最后给我一个简单的精确的对手方信息总结，如果找不到则直接返回空
"""

# 读取 Excel 文件
# df_sorted_expenses_summary = pd.read_excel(
#     "resourse/sorted_expenses_summary.xlsx", engine="openpyxl"
# )
df_sorted_income_summary = pd.read_excel(
    "resourse/sorted_income_summary.xlsx", engine="openpyxl"
)


def search_contact(contact_name):
    answer = LangchainAgent().chat(chat_template.format(contact_name))
    return answer


df_sorted_income_summary["CounterpartyDesc"] = df_sorted_income_summary[
    "Counterparty"
].apply(search_contact)


# 将 DataFrame 写入新的 Excel 文件
# df_sorted_expenses_summary.to_excel(
#     "resourse/sorted_expenses_summary_search_contact.xlsx",
#     index=False,
#     engine="openpyxl",
# )
df_sorted_income_summary.to_excel(
    "resourse/sorted_income_summary_search_contact.xlsx", index=False, engine="openpyxl"
)
