from src.infra.model.resultModel import ResultErrorModel

class GetByPersonIdAddressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('person_id')
        if not _id:
            self.add_error('person_id', 'O ID da pessoa é obrigatorio.')
            return self.valid()
        if _id and type(_id) != int:
            self.add_error('person_id', 'O ID da pessoa precisa ser inteiro.')
        return self.valid()
