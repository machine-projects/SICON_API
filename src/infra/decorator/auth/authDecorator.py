from functools import wraps
from flask_jwt_extended import get_jwt_claims, verify_jwt_in_request, get_jwt_identity
from src.repository.userProfileSystem.userProfileSystemRepository import UserProfileSystemRepository
from src.repository.profilePermission.profilePermissionRepository import ProfilePermissionRepository


class AuthDecorator:
        
    def admin_required(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            if claims['is_admin'] != True:
                return {'msg': 'Requer permissão do tipo ADMIN', 'error': True, 'data': {'result': False}}, 403
            else:
                return fn(*args, **kwargs)
        return wrapper
   
    def required_permission(self, permission_id, **options):
        
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                verify_jwt_in_request()
                user_id = get_jwt_identity()
                claims = get_jwt_claims()
                is_admin = claims.get('is_admin')
                user_id = claims.get('userId')
                if is_admin:
                    return f(*args, **kwargs)
                repository_user_profile_system = UserProfileSystemRepository()
                user_profiles = repository_user_profile_system.get_search_by_params({
                    'data': {
                        'system_id':1,
                        'user_id':user_id
                    }}
                )['data']['result']
                if not user_profiles:
                    return {'msg': 'O usuario não tem nunhum perfil com permissoões cadastradas.',
                            'error': True, 'data': {'result': False}}, 403
                profile_system_ids = [ud['profile_system_id'] for ud in user_profiles]
                repository_profile_permission = ProfilePermissionRepository()
                permissions_on = repository_profile_permission.get_multiples_profile_system_id(dict(
                    profile_system_ids=profile_system_ids
                ))['data']['result']
                permissions_ids = [p.get('system_permission_id') for p in permissions_on]
                if permissions_ids.__contains__(permission_id):
                    return f(*args, **kwargs)
                return {'msg': 'Usuario sem permissão necessaria.',
                        'error': True, 'data': {'result': False}}, 403
            return wrapper
        return decorator