from rest_framework import generics, viewsets
from city.models import City, Continent
from city.serializers import CitySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from city.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly



class CityAPIList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CityAPIUpdate(generics.UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


class CityAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdminOrReadOnly, )



# class CityViewSet(viewsets.ModelViewSet):
#     serializer_class = CitySerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return City.objects.all()[:3]
#         return City.objects.filter(pk=pk)    

#     @action(methods=['get'], detail=True)
#     def continent(self, request, pk=None):
#         continent = Continent.objects.get(pk=pk)
#         return Response({'continent': continent.name})

#     @action(methods=['get'], detail=False)
#     def continents(self, request):
#         continents = Continent.objects.all()
#         return Response({'continents': [c.name for c in continents]})