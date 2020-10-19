class Config:
    SECRET_KEY = "56we(3hev1w$n4cnja$3i4i+)-g3(o^4ow-(5c5dz-^^r0k$-&"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@192.168.99.100/themistoReports"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION='headers'


class Dev(Config):
    Debug=True
    TOKEN_DAYS_EXPIRES=10


    
class Prod(Config):
    Debug=False
    TOKEN_DAYS_EXPIRES=10

class Test(Config):
    Debug=True


config = {
    'dev': Dev,
    'prod': Prod,
    'test': Test
}