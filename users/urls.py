from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import AddressViewSet, UserViewSet, GroupViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('address', AddressViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
    