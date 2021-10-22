from rest_framework.routers import SimpleRouter

from .views import OrderViewSet, OrderItemViewSet

router = SimpleRouter()
router.register('orders', OrderViewSet)
router.register('orderitems', OrderItemViewSet)

urlpatterns = router.urls
