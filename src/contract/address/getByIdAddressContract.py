from src.infra.model.resultModel import ResultErrorModel

class GetByIdAddressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        if not _id:
            self.add_error('id', 'ID é obrigatorio.')
            return self.valid()
        if _id and type(_id) != int:
            self.add_error('id', 'ID precisa ser inteiro.')
        return self.valid()
