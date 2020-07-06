from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper

class GetByCpfPersonContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, cpf):
        helper = PersonHelper()

        if not cpf:
            self.add_error('cpf', 'CPF é obrigatorio.')
            return self.valid()
        if not helper.validate_cpf(cpf):
            self.add_error('cpf', 'CPF invalido.')
        return self.valid()
