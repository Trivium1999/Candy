from django.urls import path
from .views import RenderHomeView


urlpatterns = [
    path('', RenderHomeView.as_view())
]
