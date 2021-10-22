from rest_framework.routers import SimpleRouter

from .views import CartItemViewSet, CartViewSet

router = SimpleRouter()
router.register('carts', CartViewSet)
router.register('cartitems', CartItemViewSet)

urlpatterns = router.urls