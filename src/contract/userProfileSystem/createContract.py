from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreateUserProfileSystemContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        user_id = data.get('user_id')
        profile_system_id = data.get('profile_system_id')
        system_id = data.get('system_id')
        
        if not user_id:
            self.add_error('user_id', 'O ID do usuario é obrigatorio.')
        if user_id and type(user_id) != int:
            self.add_error('user_id', 'O ID do usuario precisa ser um inteiro.')
        if not system_id:
            self.add_error('system_id', 'O ID do sistema é obrigatorio.')
        if system_id and type(system_id) != int:
            self.add_error('system_id', 'O ID do sistema precisa ser um inteiro.')
        if not profile_system_id:
            self.add_error('profile_system_id', 'O ID do perfil do sistema é obrigatorio.')
        if profile_system_id and type(profile_system_id) != int:
            self.add_error('profile_system_id', 'O ID do perfil do sistema precisa ser um inteiro.')

        return self.valid()
