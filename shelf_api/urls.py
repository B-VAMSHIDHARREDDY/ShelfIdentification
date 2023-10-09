from django.urls import path
from .views import ShelfIdentificationView

urlpatterns = [
    path('identify-shapes/', ShelfIdentificationView.as_view(), name='identify-shapes'),
]
