from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializer import UserSerializer
import jwt
import datetime
import pandas as pd


# Create your views here.

class RegisterView( APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    
    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }
        # secret string secreto, this link generate a secret string:
        # https://www.lastpass.com/es/features/password-generator
        token = jwt.encode(payload, 'sJ3x*6O3brhnKL@fNDC*KaOJ82g4WMlC5j', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response





class UserView(APIView):
    
    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'sJ3x*6O3brhnKL@fNDC*KaOJ82g4WMlC5j', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)




class LogoutView(APIView):
    
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={
            'message': 'Success logout, cookie deleted'
        }
        return response


# class RegisterManyUsersView(APIView):

    # def post(self, request):
    #     url = 'https://docs.google.com/spreadsheets/u/3/d/1PTFUALue4Qy1MdtzaeJ37t-4HU3HwfMFAGQt3UOz6SQ/export?format=csv&id=1PTFUALue4Qy1MdtzaeJ37t-4HU3HwfMFAGQt3UOz6SQ&gid=135007174'
    #     df = pd.read_csv(url)
    #     ????????????
    #     {'total_students': len(df)}




    #     serializer = UserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

