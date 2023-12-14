""" This file is automatically generated, please do not modify """

from bankstatement_copilot.http.model.generic_response import GenericResponse
from bankstatement_copilot.http.model.ocr_bank_statement import OcrBankStatement
from bankstatement_copilot.http.model.ocr_request import OcrRequest
from .request_session import provide_request_session

from aiohttp import ClientSession


@provide_request_session
async def ocrBankStatement(data: OcrRequest, session: ClientSession = None):
    async with session.post("/ocr/bank_statement", json=data.dict()) as response:
        data = await response.json()
    resp = GenericResponse[OcrBankStatement].parse_obj(data)
    resp.data = OcrBankStatement(**resp.data)

    return resp