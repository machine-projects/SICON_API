from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByParamsPersonContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, playload):
        person_helper = PersonHelper()
        generic_helper = GenericHelper()

        cnpj = playload.get('cnpj')
        cpf = playload.get('cpf')
        birth_date = playload.get('birth_date')
        gender = playload.get('gender')
        _id = playload.get('id')
        name = playload.get('name')
        _type = playload.get('type')

        if cnpj and not person_helper.validate_cnpj(cnpj):
            self.add_error('cnpj', 'CNPJ invalido.')
        if cpf and not person_helper.validate_cpf(cpf):
            self.add_error('cpf', 'CPF invalido.')
        if birth_date and not generic_helper.str_date_check(birth_date, '-'):
            self.add_error('birth_date', 'Data de nascimento precisa estár no formato dd-mm-aaaa.')
        if gender and not (gender == 'Masculino' or gender == 'Feminino'):
            self.add_error('gender', 'O gênero precisa ser "Masculino" ou "Feminino".')
        if _id and not _id.isnumeric():
            self.add_error('id', 'O ID precisa ser um inteiro.')

        
        return self.valid()
