from django.urls import path
from .views import ShelfIdentificationView

urlpatterns = [
    path('shelf-identification/', ShelfIdentificationView.as_view(), name='identify-shapes'),
]
