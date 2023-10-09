from django.urls import path
from .views import ShelfIdentificationView

urlpatterns = [
    path('', ShelfIdentificationView.as_view(), name='identify-shapes'),
]
