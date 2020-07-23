class ValidationsAndSetStatusResultInfraHandler:

    def __init__(self):
        pass

    @staticmethod
    def default(result):
        error = result.get('error')
        if error and result.get('exeption'):
            return result, 500
        if error:
            return result, 406
        return result, 200
    
    @staticmethod
    def created(result):
        error = result.get('error')
        if error and result.get('exeption'):
            return result, 500
        if error:
            return result, 406
        return result, 201