
from django.urls import path
from api import view as local_view


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('top-movie/', local_view.top_movie),
    path('detail-movie/<int:id>', local_view.detail_movie),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
