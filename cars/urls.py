from rest_framework.routers import SimpleRouter

from cars import views


app_name = 'cars'

router = SimpleRouter()
router.register(
    prefix=r'',
    base_name='cars',
    viewset=views.CarViewSet
)
urlpatterns = router.urls
