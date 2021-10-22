from rest_framework.routers import SimpleRouter

from .views import CouponViewSet

router = SimpleRouter()
router.register('coupons', CouponViewSet)

urlpatterns = router.urls