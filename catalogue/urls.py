from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls