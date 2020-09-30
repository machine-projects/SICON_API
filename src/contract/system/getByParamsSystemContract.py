from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByParamsSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        url = data.get('url')
        
       
        if _id and type(_id) != int:
            self.add_error('_id', 'O id precisa ser um inteiro.')
        if name and type(name) != str:
            self.add_error('name', 'O nome precisa ser uma string.')
        if url and type(url) != str:
            self.add_error('url', 'O url precisa ser uma string.')
        if not _id and not name and not url:
            self.add_error('id, name, url', 'É obrigatorio o envio de nominimo um parametro.')

        return self.valid()
