from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByParamsSystemPermissionContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        system_id = data.get('system_id')
        
       
        if _id and type(_id) != int:
            self.add_error('id', 'O ID precisa ser um inteiro.')
        if system_id and type(system_id) != int:
            self.add_error('system_id', 'O ID do sistema precisa ser um inteiro.')
        if name and type(name) != str:
            self.add_error('name', 'O nome precisa ser uma string.')
        if not _id and not name and not system_id:
            self.add_error('id, name, system_id', 'É obrigatorio o envio de nominimo um parametro.')

        return self.valid()
