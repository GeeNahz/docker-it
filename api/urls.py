from django.urls import path

from .views import TodoViewSet
from rest_framework.routers import DefaultRouter


app_name = "api"

router = DefaultRouter()
router.register(r"todos", TodoViewSet, basename="todo")

urlpatterns = router.urls