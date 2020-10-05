from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByIdProfileSystemAndDependenciesContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, _id):

        if not _id:
            self.add_error('id', 'O ID do perfil é obrigatorio.')
        if _id and type(_id) != int:
            self.add_error('id', 'O ID do perfil precisa ser um inteiro.')
     
        return self.valid()
