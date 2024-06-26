from django.urls import path
from .views import (list_tasks, createHotel, deleteHotel,
                    editHotelRender, editHotel, readHotelRender, readHotel)

# Lista de rutas para la aplicación de gestión de hoteles
urlpatterns = [
    # Muestra la página principal con todos los hoteles
    path('', list_tasks, name="list_tasks"),

    # Ruta para crear un nuevo hotel mediante una solicitud POST
    path('new/', createHotel, name="createHotel"),

    # Ruta para eliminar un hotel existente por su ID
    path('delete_hotel/<int:hotel_id>/', deleteHotel, name='deleteHotel'),

    # Ruta para mostrar el formulario de edición para un hotel específico
    path('edit_hotel_Render/<int:hotel_id>/', editHotelRender, name="editHotelRender"),

    # Ruta para procesar la actualización de un hotel por su ID mediante POST
    path('edit_hotel/<int:hotel_id>/', editHotel, name="editHotel"),

    # Ruta para mostrar los detalles de un hotel específico
    path('read_hotel_Render/<int:hotel_id>/', readHotelRender, name="readHotelRender"),

    # Ruta para editar los detalles de un hotel específico (similar a `editHotel`, pero
    # podría ser usada para ver o editar detalles dependiendo del contexto)
    path('read_hotel/<int:hotel_id>/', readHotel, name="readHotel"),
]
