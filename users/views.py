from django.http import JsonResponse

from rest_framework.generics import GenericAPIView

from users.models import Users
from users.serializers import UserSerializer
from utils import encrypt


class UsersView(GenericAPIView):
    def get(self, request):
        user = request.session.get('user_info', None)
        if user:
            return JsonResponse({'user': user})
        else:
            return JsonResponse({'message': 'please login first'}, status=401)


class RegisterView(GenericAPIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return JsonResponse({'message': 'successful'}, status=201)
        else:
            print(user.errors)
            return JsonResponse({'message': user.errors}, status=400)


class LoginView(GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return JsonResponse({'message': 'username or password invalid'}, status=401)
        user = Users.objects.filter(username=username).first()
        encrypt_pwd = encrypt.md5(password)
        if user and encrypt_pwd == user.password:
            userSerializer = UserSerializer(user)
            request.session["user_info"] = userSerializer.data
            return JsonResponse({'message': 'successful', 'user': userSerializer.data})
        else:
            return JsonResponse({'message': 'username or password invalid'}, status=401)
