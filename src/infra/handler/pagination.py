
from flask import request


class Paginate:

    def __init__(self):
        pass
    
    def __valid_params(self, data, default_value):
        if not data: return default_value
        if type(data) == str:
            if data.isnumeric():
                return int(data)
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
        result = {
            'paginate': {
            'page': page, 
            'per_page': per_page
        }}
        return result

    def body_intercept_params(self, request):
        playload = request.json
        page = playload.get('page')
        per_page = playload.get('per_page')

        page = self.__valid_params(page, 1)
        per_page = self.__valid_params(per_page, 10)
        result = {
            'paginate': {
            'page': page, 
            'per_page': per_page
        }}
        return result
    
    def include_paginate_args_playload(self, request, playload={}):
        paginate = self.url_intercept_args(request)
        _filter = self.remove_paginate_items(playload)
         
        return {**_filter, **paginate}
    
    def include_paginate_params_playload(self, request, playload):
        paginate = self.body_intercept_params(request)
        _filter = self.remove_paginate_items(playload)

        return {**_filter, **paginate}

    def remove_paginate_items(self, playload):
        playload = dict(playload)
        paginate_items = ["page", "pages", "per_page", "prev_num", "total"]
        for item in paginate_items:
            if playload.get(item): playload.pop(item)
        return dict(data=playload)