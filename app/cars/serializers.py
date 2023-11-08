from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cars.models import Car
from cars.models import Manufacturer


class SearchQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=200)
    limit = serializers.IntegerField(required=False, default=2)
    offset = serializers.IntegerField(required=False, default=0)


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            "name",
            "country_code",
        )


class CarSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer()
    points = serializers.IntegerField(required=False, default=1)
    auction_title = serializers.CharField()

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "type",
            "description",
            "points",
            "color",
            "auction_title",
            "manufacturer",
        )
