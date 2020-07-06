from src.infra.model.resultModel import ResultErrorModel

class UpdatePersonAddressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        person_id = data.get('person_id')
        address_id = data.get('address_id')
        if not _id:
            self.add_error('id', 'O ID é obrigatorio.')
            return self.valid()
        if _id and type(_id) != int:
            self.add_error('id', 'O ID precisa ser inteiro.')
        if not person_id:
            self.add_error('person_id', 'O ID da pessoa é obrigatorio.')
            return self.valid()
        if person_id and type(person_id) != int:
            self.add_error('person_id', 'O ID da pessoa precisa ser inteiro.')
        if not address_id:
            self.add_error('address_id', 'O ID do endereço é obrigatorio.')
            return self.valid()
        if address_id and type(address_id) != int:
            self.add_error('address_id', 'O ID do endereço precisa ser inteiro.')
        return self.valid()
