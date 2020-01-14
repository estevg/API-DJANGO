
from django.urls import path
from api import view as local_view

urlpatterns = [
    path('top-movie/', local_view.top_movie),
    path('detail-movie/<int:id>', local_view.detail_movie),
]
