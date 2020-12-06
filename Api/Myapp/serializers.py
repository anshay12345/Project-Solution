from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    # SERIALIZES A NAME FIELD FOR TESTING OUR APIVIEW

    name = serializers.CharField(max_length=10)  # DEFINING FIELD FOR A SERIALIZER


class UserProfileSerializer(serializers.ModelSerializer):
    # A SERIALIZER FOR OUR USER PROFILE OBJECTS

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # CREATE AND RETURN A NEW USER

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])  # SETTING AND VALIDATING PASSWORD
        user.save()
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    # A SERIALIZER FOR PROFILE AND FEED ITEMS

    class Meta:
        model = models.ProfileFeedItem
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}
