from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import UniqueTogetherValidator
from finman_backend.users.models import UserPersonal

User = get_user_model()


# class UserInforRelateField(serializers.RelatedField):
#     def to_representation(self, obj):
#         return {
#             'height': obj.height,
#             'weight': obj.weight,
#             'gender': obj.gender,
#             'age': obj.age,
#             'last_update': obj.last_update
#         }


class UserRelatedField(serializers.RelatedField):

    def to_representation(self, obj):
        return {
            'email': obj.email,
            'name': obj.name,
        }

    def to_internal_value(self, data):
        try:
            user = User.objects.get(pk=data)
        except User.DoesNotExist:
            raise serializers.ValidationError('bad inventor')
        return user


class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        rep = super(UserSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep

    class Meta:
        model = User
        fields = ["email", "password", "name"]
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['email']
            )
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token


# class UserPersonalSerializer(serializers.ModelSerializer):
#     user = UserRelatedField(many=False, queryset=User.objects.all())

#     class Meta:
#         model = UserPersonal
#         fields = [
#             'height', 'weight', 'gender', 'age', 'user', 'last_update', 'create_at'
#         ]
