from django.urls import path
from .views import (list_tasks, createHotel, deleteHotel,
                    editHotelRender, editHotel, readHotelRender, readHotel,
                    obtener_detalles_hotel)

# Lista de rutas para la aplicación de gestión de hoteles
urlpatterns = [
    # Muestra la página principal con todos los hoteles
    path('', list_tasks, name="list_tasks"),

    # Ruta para crear un nuevo hotel mediante una solicitud POST
    path('new/', createHotel, name="createHotel"),

    # Ruta para eliminar un hotel existente por su ID
    path('delete_hotel/<str:hotel_id>/', deleteHotel, name='deleteHotel'),

    # Ruta para mostrar el formulario de edición para un hotel específico
    path('edit_hotel_Render/<str:hotel_id>/', editHotelRender, name="editHotelRender"),

    # Ruta para procesar la actualización de un hotel por su ID mediante POST
    path('edit_hotel/<str:hotel_id>/', editHotel, name="editHotel"),

    # Ruta para mostrar los detalles de un hotel específico
    path('read_hotel_Render/<str:hotel_id>/', readHotelRender, name="readHotelRender"),

    # Ruta para editar los detalles de un hotel específico (similar a `editHotel`, pero
    # podría ser usada para ver o editar detalles dependiendo del contexto)
    path('read_hotel/<str:hotel_id>/', readHotel, name="readHotel"),

    path('read_hotel/<int:hotel_id>/', obtener_detalles_hotel, name='obtener_detalles_hotel'),  # Ruta para la vista JSON

]
