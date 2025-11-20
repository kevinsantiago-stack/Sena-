from django.urls import path
from .views import beneficioListCreateView, beneficioRetrieveUpdateDestroyView
from .views import inicio, beneficioListCreateView, beneficioRetrieveUpdateDestroyView, inicio


urlpatterns = [
    path('inicio1/', inicio, name='inicio'),  # Vista HTML
    path('beneficio/', beneficioListCreateView.as_view(), name='beneficio-list-create'),
    path('beneficio/<int:pk>/', beneficioRetrieveUpdateDestroyView.as_view(), name='beneficio-detail'),
   

]