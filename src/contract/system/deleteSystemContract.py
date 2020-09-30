from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class DeleteSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
    
        if not _id:
            self.add_error('id', 'O ID é obrigatorio.')
        if _id and type(_id) != int:
            self.add_error('id', 'O ID precisa ser um inteiro.')

        return self.valid()
