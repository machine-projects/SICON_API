import datetime
import re

class GenericHelper:

    def __init__(self):
        pass

    def str_date_to_datetime(self, str_date):
         return datetime.datetime.strptime(str_date, '%d/%m/%Y')

    def str_date_check(self, str_date):
        return re.fullmatch(r'[0-9]{2}/[0-9]{2}/[0-9]{4}', str_date)
    
    def iso_date_to_local_date(self, date):
        if not date: return date
        iso_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return format(iso_date, "%d/%m/%Y")

    def captalize_full_str(self, string):
        if not string or type(string) != str:
            return string
        return string.title()
    
    def captalize_full_dict(self, dictionary):
        if type(dictionary) != dict:
            return dictionary
        for key in dictionary.keys():
            dictionary[key] = captalize_full_str(dictionary[key])
        return dictionary
            