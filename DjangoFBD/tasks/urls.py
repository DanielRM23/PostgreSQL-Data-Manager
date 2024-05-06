from django.urls import path
from .views import list_tasks, createHotel, deleteHotel

urlpatterns = [
    path('', list_tasks),  # Página principal
    path('new/', createHotel, name="createHotel"),
    path('delete_hotel/<int:hotel_id>/', deleteHotel, name='deleteHotel')  # Para eliminar un hotel
]