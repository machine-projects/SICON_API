from src.infra.model.resultModel import ResultErrorModel

class GetByPersonIdContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        person_id = data.get('person_id')
        if not person_id:
            self.add_error('person_id', 'O ID da pessoa é obrigatorio.')
            return self.valid()
        if person_id and type(person_id) != int:
            self.add_error('person_id', 'O ID da pessoa precisa ser inteiro.')
        return self.valid()
