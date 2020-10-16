from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreateMultiplesUserProfileSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        users_ids = data.get('users_ids')
        profile_system_id = data.get('profile_system_id')
        
        if not users_ids:
            self.add_error('users_ids', 'Os IDs dos usuarios é obrigatorio.')
        if users_ids and type(users_ids) != list:
            self.add_error('users_ids', 'Os IDs dos usuarios precisam ser uma lista.')
        if not profile_system_id:
            self.add_error('profile_system_id', 'O ID do perfil do sistema é obrigatorio.')
        if profile_system_id and type(profile_system_id) != int:
            self.add_error('profile_system_id', 'O ID do perfil do sistema precisa ser um inteiro.')

        return self.valid()
