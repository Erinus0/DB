from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # 기본 URL에서 index 뷰를 서빙
    path('<path:path>', index),      # 다른 모든 경로를 React로 서빙
]