from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreateProfilePermissionContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        profile_system_id = data.get('profile_system_id')
        system_permision_id = data.get('system_permision_id')
        
        if not profile_system_id:
            self.add_error('profile_system_id', 'O ID do perfil do sistema é obrigatorio.')
        if profile_system_id and type(profile_system_id) != int:
            self.add_error('profile_system_id', 'O ID do perfil do sistema precisa ser um inteiro.')
    
        if system_permision_id:
            self.add_error('system_permision_id', 'O ID da permissão do sistema é obrigatorio.')
        if system_permision_id and type(system_permision_id) != int:
            self.add_error('system_permision_id', 'O ID da permissão do sistema precisa ser um inteiro.')

        return self.valid()
