from src.infra.model.resultModel import ResultErrorModel

class GetUserAndpersonAndAddressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        user_id = data.get('user_id')
        person_id = data.get('person_id')
        address_id = data.get('address_id')

        if user_id and not user_id.isnumeric():
            self.add_error('user_id', 'O ID do usuario precisa ser um inteiro.')
        if person_id and not person_id.isnumeric():
            self.add_error('person_id', 'O ID da pessoa precisa ser um inteiro.')
        if address_id and not address_id.isnumeric():
            self.add_error('address_id', 'O ID do endereço precisa ser um inteiro.')


        if not (user_id or person_id or address_id):
            self.add_error('user_id', 'Parametro')
            self.add_error('person_id', 'Parametro')
            self.add_error('address_id', 'Parametro')

        return self.valid()
