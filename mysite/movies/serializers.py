from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        #defining the model which will be used to create API
        fields=['id', 'name', 'duration', 'rating']
        #defining the database columns that will be used in the API