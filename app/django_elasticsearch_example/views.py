import abc
from typing import Any
from typing import Dict

from django.http import HttpResponse
from elasticsearch_dsl.query import Bool
from elasticsearch_dsl.response import Response
from elasticsearch_dsl.search import Search
from rest_framework import status
from rest_framework.response import Response as DRFResponse
from rest_framework.views import APIView

from django_elasticsearch_example.exceptions import APIViewError
from django_elasticsearch_example.serializers import SearchQuerySerializer


class PaginatedElasticSearchAPIView(APIView):
    """
    An API view for paginating and retrieving search results from Elasticsearch.

    Attributes:
        serializer_class (type): The serializer class to use for formatting search results.
        document_class (type): The Elasticsearch document class representing the data.

    Subclasses must implement the 'generate_q_expression' method, which returns a query expression (Q()).

    Pagination Limitation:
    By default, you cannot use 'from' and 'size' to page through more than 10,000 hits.
    This limit is a safeguard set by the 'index.max_result_window' index setting.
    If you need to page through more than 10,000 hits, use more advanced solution.

    Elasticsearch docs: https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html
    """

    serializer_class = None
    document_class = None
    query_serializer_class = SearchQuerySerializer

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden and return a Q() expression."""

    def get(self, request):
        """
        Handle GET requests for paginated search results.

        This endpoint allows paginated retrieval of search results from Elasticsearch.
        Pagination parameters are expected as query parameters.

        Parameters:
        - query (str): The search query string.
        - offset (int): The starting position of the search results.
        - limit (int): The number of results to retrieve in a single page.

        Returns:
        A paginated list of search results serialized according to 'serializer_class'.

        Raises:
        - HTTP 400 Bad Request: If query parameters are invalid.
        - HTTP 500 Internal Server Error: If an error occurs during data retrieval.
        """
        search_query: SearchQuerySerializer = self.query_serializer_class(data=request.GET.dict())
        if not search_query.is_valid():
            return HttpResponse(f"Validation error: {search_query.errors}", status=status.HTTP_400_BAD_REQUEST)

        query_data: Dict[str, Any] = search_query.data
        try:
            search_query: Bool = self.generate_q_expression(query_data["query"])
            search: Search = self.document_class.search().query(search_query)

            search = search[query_data["offset"] : query_data["limit"]]
            response: Response = search.execute()

            serializer = self.serializer_class(list(response.hits), many=True)
            return DRFResponse(serializer.data, status=status.HTTP_200_OK)
        except APIViewError:
            return HttpResponse("Error during fetching data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
