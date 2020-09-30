

class Paginate:

    def __init__(self):
        pass
    
    def __valid_params(self, data, default_value):
        if not data: data = default_value
        if type(data) == str:
            if data.isnumeric():
                data = int(data)
            else:
                data = default_value
        elif type(data) != int and type(data) != str:
            data = default_value
        return data

    def url_intercept_args(self, request):
        arg = request.args
        page = arg.get('page')
        per_page = arg.get('per_page')

        page = self.__valid_params(page, 1)
        per_page = self.__valid_params(per_page, 10)
        
        return dict(page=page, per_page=per_page)

    def body_intercept_params(self, request):
        playload = request.json
        page = playload.get('page')
        per_page = playload.get('per_page')

        page = self.__valid_params(page, 1)
        per_page = self.__valid_params(per_page, 10)
        
        return dict(page=page, per_page=per_page)
    
    def include_paginate_args_playload(self, request, playload={}):
        paginate = self.url_intercept_args(request)
        return {**playload, **paginate}
    
    def include_paginate_params_playload(self, request, playload):
        paginate = self.body_intercept_params(request)
        return {**playload, **paginate}