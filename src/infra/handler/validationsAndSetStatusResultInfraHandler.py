class ValidationsAndSetStatusResultInfraHandler:

    def __init__(self):
        pass

    @staticmethod
    def default_result(result):
        if result['error'] and result['exeption']:
            return result, 500
        if result['error']:
            return result, 406
        return result, 200