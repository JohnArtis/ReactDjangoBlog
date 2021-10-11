from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostApiList

router = SimpleRouter()
router.register('', PostApiList, basename='posts')

urlpatterns = router.urls