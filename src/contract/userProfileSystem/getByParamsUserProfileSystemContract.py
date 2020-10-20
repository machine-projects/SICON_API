from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByParamsUserProfileSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        user_id = data.get('user_id')
        profile_system_id = data.get('profile_system_id')
        system_id = data.get('system_id')

        if _id and not _id.isnumeric():
            self.add_error('_id', 'O ID precisa ser um inteiro.')
        if system_id and not system_id.isnumeric():
            self.add_error('system_id', 'O ID do sistema precisa ser um inteiro.')
        if user_id and not user_id.isnumeric():
            self.add_error('user_id', 'O ID do usuario precisa ser um inteiro.')
        if profile_system_id and not profile_system_id.isnumeric():
            self.add_error('profile_system_id', 'O ID do perfil do sistema precisa ser um inteiro.')
        if not _id and not user_id and not profile_system_id:
            self.add_error('id, user_id, profile_system_id, system_id', 'É obrigatorio o envio de no minimo um parametro.')

        return self.valid()
