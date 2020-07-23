
from src.infra.model.resultModel import ResultModel


class TokenHandler:

    def __init__(self):
        pass

    def validation_token(self):
        return ResultModel('Token Valido', True, False).to_dict(), 200