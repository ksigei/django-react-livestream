from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Livestream, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        queryset = User.objects.all()

class LivestreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestream
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'