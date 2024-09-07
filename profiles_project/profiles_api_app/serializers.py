from rest_framework import serializers
from . import models

class HelloSerialzer(serializers.Serializer):
    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):
    """a serializer for our user profile object"""
    """that's simply saying the profile user will use through the API id , name, email, password but the password should be write only """
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

        def create(self, validated_data):
            """ Create and Return new user """
            user = models.UserProfile(
                email= validated_data["email"],
                name= validated_data["name"],
            )
            user.set_password(validated_data['password'])

            user.save()
            return user



