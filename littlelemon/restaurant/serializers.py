from rest_framework import serializers
from .models import BookingModel, MenuModel


class BookingSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='menu-detail')
    class Meta:
        model = BookingModel
        fields = ['id', 'url', 'name', 'number_of_guests', 'booking_date']
        
class MenuSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')
    
    class Meta:
        model = MenuModel
        fields = ['url', 'id', 'title', 'price', 'inventory']