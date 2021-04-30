from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
