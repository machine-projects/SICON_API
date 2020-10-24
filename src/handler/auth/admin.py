from flask_jwt_extended import get_jwt_claims


class Admin:

    def __init__(self):
        pass

    def is_admin(self):
        claims = get_jwt_claims()
        if claims.get('is_admin'): return True
        return False