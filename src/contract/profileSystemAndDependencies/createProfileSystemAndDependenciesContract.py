from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreateProfileSystemAndDependenciesContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        # PROFILE SYSTEM
        system_id = data.get('system_id')
        name_profile_system = data.get('name_profile_system')
        description_profile_system = data.get('description_profile_system')
        #  PROFILE PERMISSION
        system_permissions_id = data.get('system_permissions_id')
        #  USER PROFILE SYSTEM
        users_ids = data.get('users_ids')
        
        # PROFILE SYSTEM

        if not system_id:
            self.add_error('system_id', 'O ID do sistema é obrigatorio.')
        if system_id and type(system_id) != str:
            self.add_error('system_id', 'O ID do sistema precisa ser um inteiro.')
        if not name_profile_system:
            self.add_error('name_profile_system', 'O nome do perfil é obrigatorio.')
        if name_profile_system and type(name_profile_system) != str:
            self.add_error('name_profile_system', 'O nome do perfil precisa ser uma string.')
        if description_profile_system and type(description_profile_system) != str:
            self.add_error('description_profile_system', 'O descrição do perfil precisa ser uma string ou null.')

        #  PROFILE PERMISSION
        if system_permissions_id:
            self.add_error('system_permissions_id', 'Os IDs de permissões de sistema é obrigatorio.')
        if system_permissions_id and type(system_permissions_id) != list:
            self.add_error('system_permissions_id', 'Os IDs de permissões de sistema precisa estar em uma lista.')
        else:
            for system_permission_id in system_permissions_id:
                if type(system_permission_id) != int:
                    self.add_error('system_permissions_id', 'Os IDs da permissão precisa ser inteiros.')
                    break
        
        
        #  USER PROFILE SYSTEM
        if users_ids:
            self.add_error('users_ids', 'Os IDs de usuarios é obrigatorio.')
        if users_ids and type(users_ids) != list:
            self.add_error('users_ids', 'Os IDs de usuarios precisa estar em uma lista.')
        else:
            for user_id in users_ids:
                if type(user_id) != int:
                    self.add_error('users_ids', 'Os IDs de usuarios precisam ser inteiros.')
                    break
            

        

        return self.valid()
