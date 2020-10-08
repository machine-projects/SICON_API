from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByParamsProfileSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        system_id = data.get('system_id')
        

        if _id and not _id.isnumeric():
            self.add_error('_id', 'O id precisa ser um inteiro.')
        if name and type(name) != str:
            self.add_error('name', 'O nome precisa ser uma string.')
        if description and type(description) != str:
            self.add_error('description', 'A descrição precisa ser uma string.')
        if system_id and not system_id.isnumeric():
            self.add_error('system_id', 'O ID do sistema precisa ser um inteiro.')

        if not _id and not name and not description and not system_id:
            self.add_error('id, name, description, system_id', 'É obrigatorio o envio de no minimo um parametro.')
        return self.valid()
