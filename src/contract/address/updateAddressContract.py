from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper

class UpdateAdressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        helper = PersonHelper()

        _id = data.get('id')
        person_id = data.get('person_id')
        neighborhood = data.get('neighborhood')
        street = data.get('street')
        number = data.get('number')
        complement = data.get('complement')
        city = data.get('city')

        if not _id:
            self.add_error('id', 'ID é obrigatorio.')
        if _id and type(_id) != int:
            self.add_error('id', 'ID precisa ser um inteiro.')
        if not person_id:
            self.add_error('person_id', 'O ID da pessoa é obrigatorio.')
        if person_id and type(person_id) != int:
            self.add_error('person_id', 'O ID da pessoa precisa ser um inteiro.')
        if not (neighborhood == None or type(neighborhood) == str):
            self.add_error('neighborhood', 'O bairro precisa ser uma string ou null.')
        if not (street == None or type(street) == str):
            self.add_error('street', 'A rua precisa ser uma string ou null.')
        if not (number == None or type(number) == str):
            self.add_error('number', 'O número precisa ser uma string ou null.')
        if not (complement == None or type(complement) == str):
            self.add_error('complement', 'O complemento precisa ser uma string ou null.')
        if not (city == None or type(city) == str):
            self.add_error('city', 'O cidade precisa ser uma string ou null.')

        return self.valid()
