from django.urls import path

from cars.views import CarSearchAPIView

app_name = "cars"

urlpatterns = [
    path("", CarSearchAPIView.as_view()),
]
