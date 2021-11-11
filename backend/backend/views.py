from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from rest_framework import generics,mixins, status
from django.http.response import JsonResponse
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
class Login(generics.GenericAPIView):
    def post(self,request):
       data = JSONParser().parse(request)
       print(data)
       try:
           user = authenticate(username=data['username'],password=data['password'])
           resp={ }
           if user is None:
               resp ={
                   "error":"Invalid username or Password"
               }
               return JsonResponse(resp,safe=False,status=401)
           token,created=Token.objects.get_or_create(user=user)
           print("The token is -:",token)
           if user.is_staff == True:
               resp = {
                   'id':user.id,
                   'username':user.username,
                   'group':'BackendisAdmin',
                   'token':token.key,
               }
               return JsonResponse(resp,safe=False,status = 200)
           resp={
               'id':user.id,
               'username':user.username,
               'group':'FrontUser',
               'token':token.key,
           }
           return JsonResponse(resp,safe=False,status=200)
       except User.DoesNotExist:
           resp= {
               "error":"Invalid Username or Password"
           }
           return JsonResponse(resp , safe=False ,status =401)
class Logout(generics.GenericAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            Tokn = str(request.headers['Authorization']).split(' ')[1]
            print(Tokn)
            Token.objects.get(key=Tokn).delete()
        except Token.DoesNotExist:
            pass
        finally:
            resp ={
                "success":"Logout Succesfully"
            }
            return JsonResponse(resp,safe=False,status=200)
        









