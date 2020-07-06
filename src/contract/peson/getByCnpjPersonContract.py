from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper

class GetByCnpjPersonContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, cnpj):
        helper = PersonHelper()
        if not cnpj:
            self.add_error('cnpj', 'CNPJ é obrigatorio.')
            return self.valid()
        if not helper.validate_cnpj(cnpj):
            self.add_error('cnpj', 'CNPJ invalido.')
        return self.valid()
