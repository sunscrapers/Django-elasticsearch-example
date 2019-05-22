from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from cars.documents import CarDocument


class CarDocumentSerializer(DocumentSerializer):
    class Meta:
        document = CarDocument
        fields = (
            'id',
            'name',
            'type',
            'description',
            'points',
            'color',
            'auction_title',
            'manufacturer',
        )
