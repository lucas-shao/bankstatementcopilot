from pydantic import BaseModel
from typing import Generic, TypeVar

from bankstatement_copilot.http.model.ocr_bank_statement_line import (
    OcrBankStatementLine,
)


class OcrBankStatement(BaseModel):
    openingBalance: str = None
    endingBalance: str = None
    accountNumber: str = None
    sortCode: str = None
    bankStatementLineList: list[OcrBankStatementLine] = None
