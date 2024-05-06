from django.urls import path
from .views import list_tasks, createHotel, deleteHotel, editHotelRender, editHotel

urlpatterns = [
    # Página principal
    path('', list_tasks),
    # Para crear un hotel
    path('new/', createHotel, name="createHotel"),
    # Para eliminar un hotel
    path('delete_hotel/<int:hotel_id>/', deleteHotel, name='deleteHotel'),
    # Render para editar un hotel
    path('edit_hotel_Render/<int:hotel_id>/', editHotelRender, name="editHotelRender"),
    # Para editar un hotel
    path('edit_hotel/<int:hotel_id>/', editHotel, name="editHotel"),

]