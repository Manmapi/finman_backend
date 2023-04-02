from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from finman_backend.users.api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialConnectView, SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


User = get_user_model()

#
# @api_view(['POST'])
# @permission_classes([])
# def login_user(request):
#     body = request.POST
#     email = body['email']
#     password = body['password']
#
#     try:
#         user = User.objects.get(email=email)
#     except ObjectDoesNotExist:
#         return Response(data="Can not found user with this email", status=status.HTTP_404_NOT_FOUND)
#     if authenticate(username=email, password=password):
#         token = MyTokenObtainPairSerializer.get_token(user)
#         user.last_login = timezone.now()
#         user.save()
#         return Response(data={
#             'message': 'Login successfully',
#             'refresh': str(token),
#             'access': str(token.access_token),
#         }, status=status.HTTP_200_OK)
#     else:
#         return Response(data="Wrong password", status=status.HTTP_403_FORBIDDEN)
#
#
# @api_view(['POST'])
# @permission_classes([])
# def sign_up(request):
#     body = request.POST
#     serialize = UserSerializer(data=body)
#     try:
#         serialize.is_valid(raise_exception=True)
#         email = serialize.validated_data['email']
#         password = serialize.validated_data['password']
#         name = serialize.validated_data['name']
#         user = User.objects.create_user(email=email, password=password, name=name)
#         token = MyTokenObtainPairSerializer.get_token(user)
#         return Response(data={
#             'message': 'User create successfully',
#             'refresh': str(token),
#             'access': str(token.access_token),
#         }, status=status.HTTP_201_CREATED)
#     except IntegrityError as e:
#         return Response(data=json.dumps(e), status=status.HTTP_409_CONFLICT)
#
#
# class MyTokenRefreshView(TokenRefreshView):
#     permission_classes = ([])
#
#     def post(self, request, *args, **kwargs):
#
#         serializer = self.get_serializer(data=request.data)
#
#         try:
#             serializer.is_valid(raise_exception=True)
#         except TokenError as e:
#             raise InvalidToken(e.args[0])
#         body_response = serializer.validated_data
#         body_response['message'] = 'Refresh token successfully'
#         body_response['refresh'] = QueryDict.dict(request.data)['refresh']
#         return Response(body_response, status=status.HTTP_200_OK)
#
#
# token_refresh = MyTokenRefreshView.as_view()
#


# class UserPersonalCreateView(APIView):
#     permission_classes = [IsAuthenticated, IsCorrectUser]

#     def get(self, request):
#         try:
#             user_detail = UserPersonal.objects.get(user=request.user)
#             serializer = UserPersonalSerializer(user_detail)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except UserPersonal.DoesNotExist:
#             user = request.user
#             return Response({
#                 "height": None,
#                 "weight": None,
#                 "gender": None,
#                 "age": None,
#                 "user": {
#                     "email": user.email,
#                     "name": user.name,
#                 },
#             }, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.POST.copy()
#         data['user'] = request.user.pk
#         serializer = UserPersonalSerializer(data=data)

#         if 'name' in data:
#             request.user.name = data['name']
#             request.user.save()
#         if serializer.is_valid():
#             try:
#                 user_information = UserPersonal.objects.get(user=request.user)
#                 user_information.delete()
#                 serializer.save()
#             except UserPersonal.DoesNotExist:
#                 serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserPersonalDetailView(APIView):
    # permission_classes = [IsAuthenticated, IsCorrectUser]

    # def get_user_infor(self, request):
    #     try:
    #         return UserPersonal.objects.get(user=request.user)
    #     except UserPersonal.DoesNotExist:
    #         return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    # def put(self, request):
    #     user_detail = self.get_user_infor(request)
    #     data = request.data.copy()
    #     if 'name' in data:
    #         request.user.name = data['name']
    #         request.user.save()
    #     data['user'] = request.user.pk
    #     serializer = UserPersonalSerializer(user_detail, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request):
    #     user = self.get_user_infor(request)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class ListUserPersonal(ListAPIView):
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     queryset = UserPersonal.objects.all()
#     serializer_class = UserPersonalSerializer


class ListUser(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'https://api.manmapi.com/accounts/google/login/callback/'
    client_class = OAuth2Client
