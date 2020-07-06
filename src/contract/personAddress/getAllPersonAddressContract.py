from src.infra.model.resultModel import ResultErrorModel

class GetAllPersonAddressContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):

        return self.valid()
