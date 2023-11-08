from cars.views import CarSearchAPIView
from django.urls import path

app_name = "cars"

urlpatterns = [
    path("", CarSearchAPIView.as_view(), name="cars-api"),
]
