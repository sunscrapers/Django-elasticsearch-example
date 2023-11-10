from elasticsearch_dsl import Q

from cars.documents import CarDocument
from cars.serializers import CarSerializer
from django_elasticsearch_example.views import ElasticSearchAPIView


class CarSearchAPIView(ElasticSearchAPIView):
    serializer_class = CarSerializer
    document_class = CarDocument

    def elasticsearch_query_expression(self, query):
        return Q(
            "bool",
            should=[
                Q("match", name=query),
                Q("match", color=query),
                Q("match", description=query),
            ],
            minimum_should_match=1,
        )
