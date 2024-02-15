from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuModel, BookingModel
from .serializers import BookingSerializer, MenuSerializers
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [IsAuthenticated]


class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [IsAuthenticated]
    
    
class BookingViewSet(ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    
class BookingsView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class SingleBookingsView(generics.RetrieveUpdateDestroyAPIView):
    queryset =BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    






# Create your views here.

# def index(request):
#     return render(request, "index.html", {})


# class BookingView(APIView):
#     def get(self, request):
#         items = BookingModel.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
    
    
# class MenuView(APIView):
    
#     def post(self, request):
#         serializer = MenuSerializers(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         else:
#             return Response({"msg": "invalid data"}, status.HTTP_400_BAD_REQUEST)
        
    