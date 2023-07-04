from rest_framework import serializers

from apps.users.models import User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined')
        # fields = "__all__"

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=20, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=20, write_only=True
    )
    class Meta:
        model = User 
        fields = ('username', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['confirm_password'])
        user.save()
        return user