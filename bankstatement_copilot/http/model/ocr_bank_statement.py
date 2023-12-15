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


class OcrHungryPandaPaymentStatement(BaseModel):
    recipientName: str = None
    statementNumber: str = None
    orderPeriod: str = None
    foodOrderValueNormalAndRefundAmount: str = None
    foodOrderValueVoucherAndRefundAmount: str = None
    commissionNormalAndRefundAmount: str = None
    commissionVoucherAndRefundAmount: str = None
    vatNormalAndRefundAmount: str = None
    vatVoucherAndRefundAmount: str = None
    discountMerchantNormalAndRefundAmount: str = None
    discountMerchantVoucherAndRefundAmount: str = None
    deliveryFeeNormalAndRefundAmount: str = None
    deliveryFeeVoucherAndRefundAmount: str = None
    merchantOtherIncomeNormalAndRefundAmount: str = None
    merchantOtherIncomeVoucherAndRefundAmount: str = None
    adjustmentNormalAndRefundAmount: str = None
    adjustmentVoucherAndRefundAmount: str = None
    netPaymentNormalAndRefundAmount: str = None
    netPaymentVoucherAndRefundAmount: str = None
    creditAmount: str = None
    totalPaymentAmount: str = None
