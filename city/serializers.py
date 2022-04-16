from django.shortcuts import render
from rest_framework import serializers
from city.models import City
from rest_framework.renderers import JSONRenderer


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('title', 'content', 'continent', 'created')



