from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreateProfilePermissionContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        profile_system_id = data.get('profile_system_id')
        system_permisions_id = data.get('system_permisions_id')
        
        if not profile_system_id:
            self.add_error('profile_system_id', 'O ID do perfil do sistema é obrigatorio.')
        if profile_system_id and type(profile_system_id) != int:
            self.add_error('profile_system_id', 'O ID do perfil do sistema precisa ser um inteiro.')
    
        if system_permisions_id:
            self.add_error('system_permisions_id', 'Os IDs de permissão do sistema é obrigatorio.')
        if system_permisions_id and type(system_permisions_id) != list:
            self.add_error('system_permisions_id', 'Os IDs de permissão do sistema precisa ser uma lista.')

        if system_permisions_id  and type(system_permisions_id) == list:
            for system_permision_id in system_permisions_id:
                if not system_permision_id:
                    self.add_error('system_permisions_id', 'É obrigatorio ter no minimo um id na lista.')
                if system_permision_id and type(system_permision_id) != int:
                    self.add_error('system_permisions_id', 'Os IDs da lista de perfil do sistema precisam ser inteiros.')

        return self.valid()
