from src.infra.model.resultModel import ResultErrorModel


class CreateUserContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, playload):

        username = playload.get('username')
        password = playload.get('password')
        person_id = playload.get('person_id')

        if not person_id:
            self.add_error('person_id', 'O ID da pessoa é obrigatorio.')
        if person_id and type(person_id) != type(1):
            self.add_error('person_id', 'O ID da pessoa precisa ser um inteiro.')
        
        if not username:
            self.add_error('username', 'username é obrigatorio.')
        if username and type(username) != type(''):
            self.add_error('username', 'username precisa ser uma string.')
        if type(playload.get('is_admin')) != type(True):
            self.add_error('is_admin', 'is_admin é obrigatorio.')
        if not password:
            self.add_error('password', 'password é obrigatorio.')
        if password and type(password) != type(''):
            self.add_error('password', 'password precisa ser uma string.')
        
        return self.valid()
