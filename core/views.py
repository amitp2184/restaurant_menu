from django.shortcuts import render
from core.serializers import *
from core.utils import generate_access_token, generate_refresh_token
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from core.authentication import *

# Create your views here.
class UserSignUpView(CreateAPIView):
    permission_classes= []
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()
    def post(self, request, format='json'):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():

            email = serializer.validated_data['email']
            username = serializer.validated_data['username']     
            password = serializer.validated_data['password']    
            check_email = UserAccount.objects.filter(email=email).first()
            check_username = UserAccount.objects.filter(username=username).first()

            if check_username:
                return Response({"responseCode": 0,
                        "responseMessage": "User name Already Exist.",
                        "responseData": {'username':username}},
                    status=status.HTTP_200_OK)

            if check_email:
                return Response({"responseCode": 0,
                        "responseMessage": "Email Address Already Exist.",
                        "responseData": {'email':email}},
                    status=status.HTTP_200_OK)

            user = serializer.save()

            user.set_password(password)
            # user.email_verification_code_expiry = datetime.datetime.now() 
            # user.email_verification_code = random.randint(0000, 9999)          
            user.save()
            token_data = generate_access_token(user)
            data  = serializer.data
           
            return Response({"responseCode": 1,
                    "responseMessage": "Your Account has been created Successfully",
                    "responseData": {
                        'id':user.id,
                        'email': user.email,
                        'username' :user.username,                          
                        'token' :token_data,
                        
                    }},
                status=status.HTTP_200_OK)
           
        else:
            return Response({"responseCode": 0,
                        "responseMessage": "Invalid Data",
                        "responseData": serializer.errors},
                    status=status.HTTP_200_OK)

class UserSignInView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()
   

    def post(self, request, format='json'):
        try :
            serializer = UserAccountSerializer(data=request.data,context={'request':request})
            if 'email' in request.data:
                user = MyBackend.authenticate(email=request.data['email'], password=request.data['password'])
                if user is not None:
                    data = generate_access_token(user)
                    
                    return Response({"responseCode": 1,
                        "responseMessage": "You are login successfully",
                        "responseData": {
                            # 'user_id':user.id,
                            'email': user.email,
                           
                            'token' :data,
                        }},
                    status=status.HTTP_200_OK)
                else:
                    return Response({"responseCode": 0,
                                "responseMessage": "email or Password Invalid!",
                                "responseData": None},
                            status=status.HTTP_200_OK)
            return Response({"responseCode": 0,
                                "responseMessage": "Username or Password Invalid!",
                                "responseData": None},
                            status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"responseCode": 0,
                                "responseMessage": "User Not Found",
                                "responseData": None},
                            status=status.HTTP_200_OK)
