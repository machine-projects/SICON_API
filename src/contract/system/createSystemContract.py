from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreateSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        name = data.get('name')
        description = data.get('description')
        url = data.get('url')
        
        if not name:
            self.add_error('name', 'O nome é obrigatorio.')
        if name and type(name) != str:
            self.add_error('name', 'O nome precisa ser uma string.')
        if not url:
            self.add_error('url', 'O url é obrigatorio.')
        if url and type(url) != str:
            self.add_error('url', 'O url precisa ser uma string.')
        if description and type(description) != str:
            self.add_error('description', 'O descrição precisa ser uma string ou null.')

        return self.valid()
