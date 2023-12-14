import os
import asyncio

from bankstatement_copilot.http.bkp_client import ocrBankStatement
from bankstatement_copilot.http.model.ocr_request import OcrRequest


async def main():
    ocrRequest = OcrRequest()
    ocrRequest.secret_key = (
        "qI4dqCZaw0tkmwpMKrtAJ6NWabCsboPGb7wT1EUL4ohBaczIcdNac9su9NSOeGJuLH"
    )
    ocrRequest.file_path = (
        "https://oss.xiaocichang.com/file/20231114/attachment%20TIDE%20JUL.pdf"
    )
    res = await ocrBankStatement(ocrRequest)
    print(res)
    print(res.data.openingBalance)


asyncio.run(main())
