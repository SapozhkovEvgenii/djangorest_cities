from city.models import City
from city.serializers import CitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class CityApiView(APIView):

    """view class based on base class APIView"""
    
    def get(self, request):
        records_all = City.objects.all()
        return Response({"cities": CitySerializer(records_all, many=True).data})

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"city": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method PUT not allowed"})
        try:
            instance = City.objects.get(pk=pk)
        except:
            return Response({'error': "Object does not exists"})
        serializer = CitySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'city': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method DELETE not allowed"})
        try:
            instance = City.objects.get(pk=pk)
            title = str(instance)
        except:
            return Response({'error': "Object does not exists"})
        instance.delete()
        return Response({"info": "delete post " + title}) 