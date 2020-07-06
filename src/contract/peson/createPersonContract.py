from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class CreatePersonContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _type = data.get('type')
        birth_date = data.get('birth_date')
        name = data.get('name')
        surname = data.get('surname')
        gender = data.get('gender')
        cpf = data.get('cpf')
        company_name = data.get('company_name')
        cnpj = data.get('cnpj')
        
        helper = PersonHelper()
        generic_helper = GenericHelper()
        if not _type:
            self.add_error('type', 'Type é obrigatorio.')
        if _type and type(_type) != str:
            self.add_error('type', 'Type precisa ser uma string.')
        if not (birth_date == None or type(birth_date) == str):
            self.add_error('birth_date', 'A data de nascimento precisa ser uma string ou null.')
        if birth_date and not generic_helper.str_date_check(birth_date):
            self.add_error('birth_date', 'A data de nascimento precisa estar no formato dd/mm/yyyy.')
        if not (name == None or type(name) == str):
            self.add_error('name', 'Name precisa ser uma string ou null.')
        if not (surname == None or type(surname) == str):
            self.add_error('surname', 'Surname precisa ser uma string ou null.')
        if not (gender == None or type(gender) == str):
            self.add_error('gender', 'Gender precisa ser uma string ou null.')
        if not (cpf == None or type(cpf) == str):
            self.add_error('cpf', 'CPF precisa ser uma string ou null.')
        if cpf and type(cpf) == str and not helper.validate_cpf(cpf):
            self.add_error('cpf', 'CPF invalido.')
        if not (company_name == None or type(company_name) == str):
            self.add_error('company_name', 'Company name precisa ser uma string ou null.')
        if not (cnpj == None or type(cnpj) == str):
            self.add_error('cnpj', 'CNPJ precisa ser uma string ou null.')
        if cnpj and type(cnpj) == str and not helper.validate_cnpj(cnpj):
            self.add_error('cnpj', 'CNPJ invalido.')
        return self.valid()
