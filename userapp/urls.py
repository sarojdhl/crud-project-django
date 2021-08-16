from rest_framework import routers
from userapp.api import UserAPI


router = routers.SimpleRouter()
router.register(r"user", UserAPI)

urlpatterns = router.urls