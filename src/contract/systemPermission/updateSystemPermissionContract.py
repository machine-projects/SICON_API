from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class UpdateSystemPermissionContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        system_id = data.get('system_id')
        
        if not _id:
            self.add_error('id', 'O ID é obrigatorio.')
        if _id and type(_id) != int:
            self.add_error('id', 'O ID precisa ser um inteiro.')
        if not name:
            self.add_error('name', 'O nome é obrigatorio.')
        if name and type(name) != str:
            self.add_error('name', 'O nome precisa ser uma string.')
        if not system_id:
            self.add_error('system_id', 'O ID do sistema é obrigatorio.')
        if system_id and type(system_id) != int:
            self.add_error('system_id', 'O ID do sistema precisa ser um inteiro.')
        if description and type(description) != str:
            self.add_error('description', 'O descrição precisa ser uma string ou null.')

        return self.valid()
