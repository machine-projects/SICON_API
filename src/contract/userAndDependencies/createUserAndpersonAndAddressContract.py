from src.infra.model.resultModel import ResultErrorModel
from src.contract.peson.createPersonContract import CreatePersonContract
from src.contract.address.createAddressContract import CreateAdressContract

class CreateUserAndpersonAndAddressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        user = data.get('user')
        person = data.get('person')
        address = data.get('address')

        contract_person = CreatePersonContract()
        contract_address = CreateAdressContract()
        


        if not user: 
            self.add_error('user', 'user é obrigatorio.') 
            

        person = data.get('person')
        if not person:
            self.add_error('username', 'username é obrigatorio.')

        if not user or not person: return self.valid()


        username = user.get('username')
        password = user.get('password')

        if not username:
            self.add_error('username', 'username é obrigatorio.')
        if username and type(username) != type(''):
            self.add_error('username', 'username precisa ser uma string.')
        if user.get('is_admin') and type(user.get('is_admin')) != type(True):
            self.add_error('is_admin', 'is_admin precisa ser booleano.')
        if not password:
            self.add_error('password', 'password é obrigatorio.')
        if password and type(password) != type(''):
            self.add_error('password', 'password precisa ser uma string.')

        type_person = person.get('type')
        if not type_person: self.add_error('type', 'typeé obrigatorio.')
        if type_person and type(type_person) != type(''):
            self.add_error('type', 'type precisa ser uma string.')

        if not contract_person.validate(person):            
            self.errors = [*self.errors, *contract_person.errors]
        
        # address
        neighborhood = address.get('neighborhood')
        street = address.get('street')
        number = address.get('number')
        complement = address.get('complement')
        city = address.get('city')
        
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
