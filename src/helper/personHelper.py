


class PersonHelper:

    def validate_cpf(self, cpf):
        cpf = self.remove_characters(cpf)
        if len(cpf) < 11:
            return False    
        
        if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
            return False
        
        calc = lambda t: int(t[1]) * (t[0] + 2)
        d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
        d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
        return str(d1) == cpf[-2] and str(d2) == cpf[-1]


    def validate_cnpj(self, cnpj ):
        list_validate_one = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4 , 3, 2]
        list_validate_two = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
        # cleaning the cnpj
        cnpj = self.remove_characters(cnpj)
        # finding out the digits
        verify = cnpj[-2:]
        # verifying the lenght of the cnpj
        if len( cnpj ) != 14:
            return False
        # calculating the first digit
        _sum = 0
        id = 0
        for num in cnpj:
            # to do not raise indexerrors
            try:
                list_validate_one[id]
            except:
                break
            _sum += int( num ) * int( list_validate_one[id] )
            id += 1
        _sum = _sum % 11
        if _sum < 2:
            character_one = 0
        else:
            character_one = 11 - _sum
        character_one = str( character_one ) # converting to string, for later comparison
        # calculating the second digit
        # suming the two lists
        _sum = 0
        id = 0
        # suming the two lists
        for num in cnpj:
            # to do not raise indexerrors
            try:
                list_validate_two[id]
            except:
                break
            _sum += int( num ) * int( list_validate_two[id] )
            id += 1
        # defining the digit
        _sum = _sum % 11
        if _sum < 2:
            character_two = 0
        else:
            character_two = 11 - _sum
        character_two = str( character_two )
        # returnig
        return bool( verify == character_one + character_two )

    @staticmethod
    def remove_characters(data):
        data = data.replace( "-", "" )
        data = data.replace( ".", "" )
        data = data.replace( "/", "" )
        return data