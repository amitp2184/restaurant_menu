from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.db.models import Q
from employee.models import *

import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
# from account.models import *


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


class SafeJWTAuthentication(BaseAuthentication):
    '''
        custom authentication class for DRF and JWT
        https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
    '''

    def authenticate(self, request):

        user = UserAccount.objects.all()
        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
       
        user = UserAccount.objects.filter(email=payload['user_email']).first()
        
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        # if not user.is_active:
        #     raise exceptions.AuthenticationFailed('user is inactive')

        # self.enforce_csrf(request)
        return (user, None)



class SafeAuthJWTAuthentication(BaseAuthentication):
    '''
        custom authentication class for DRF and JWT
        https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
    '''

    def authenticate(self, request):

        user = Employee.objects.all()
        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
       
        user = Employee.objects.filter(email=payload['user_email']).first()
        
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        # if not user.is_active:
        #     raise exceptions.AuthenticationFailed('user is inactive')

        # self.enforce_csrf(request)
        return (user, None)

    # def enforce_csrf(self, request):
    #     """
    #     Enforce CSRF validation
    #     """
    #     check = CSRFCheck()
    #     # populates request.META['CSRF_COOKIE'], which is used in process_view()
    #     check.process_request(request)
    #     reason = check.process_view(request, None, (), {})
    #     print(reason)
    #     if reason:
    #         # CSRF failed, bail with explicit error message
    #         raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)


class MyBackend(BaseBackend):
    def authenticate(email=None, password=None):
        
        login_valid = UserAccount.objects.get(Q(username__iexact=email) | Q(email__iexact=email))

        pwd_valid = check_password(password, login_valid.password)
        if login_valid and pwd_valid:
            try:
                user = UserAccount.objects.get(Q(username__iexact=email) | Q(email__iexact=email))
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = UserAccount(email=email)
                user.save()
            return user
        return None
    
class MyBackendWithUser(BaseBackend):
    def authenticate(email=None, password=None):
        
        login_valid = Employee.objects.get(email=email)

        pwd_valid = check_password(password, login_valid.password)
        if login_valid and pwd_valid:
            try:
                user = Employee.objects.get(email=email)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(email=email)
                # user.save()
            return user
        return None