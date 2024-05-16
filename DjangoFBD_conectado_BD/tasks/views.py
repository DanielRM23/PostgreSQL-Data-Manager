from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Hotel
from django.http import JsonResponse  # Para devolver respuestas JSON

def list_tasks(request):
    '''
    Muestra todos los hoteles disponibles.

    Esta función obtiene todos los objetos 'Hotel' almacenados en la base de datos y
    los proporciona al contexto para renderizar la plantilla 'list_tasks.html'.

    :param request: Una instancia del objeto HttpRequest que representa la solicitud del cliente.
    :return: Una respuesta HTTP con el contenido renderizado de 'list_tasks.html',
             incluyendo todos los hoteles disponibles en el contexto.
    '''
    Hotels = Hotel.objects.all()  # Obtiene todos los objetos Hotel de la base de datos
    return render(request, "list_tasks.html", {'Hotels': Hotels})  # Renderiza la vista con el contexto de los hoteles



def createHotel(request):
    '''
    Crea un nuevo hotel con datos proporcionados en una solicitud POST.

    Esta función espera que la solicitud sea de tipo POST y contenga ciertos campos
    requeridos para crear un nuevo objeto 'Hotel'. Verifica que todos los campos necesarios
    estén presentes y, si alguno falta, devuelve una respuesta de error. Si todos los
    campos están presentes, se crea un nuevo objeto 'Hotel' y se guarda en la base de datos.
    Tras el guardado exitoso, se redirige a la página de inicio.

    :param request: Una instancia de HttpRequest que representa la solicitud entrante desde el cliente.
    :return: Una respuesta HTTP que puede ser:
             - HTTP 302 para redirigir a la página de inicio tras guardar con éxito.
             - HTTP 400 si falta algún campo requerido o la solicitud no es de tipo POST.
    '''
    if request.method == 'POST':  # Verifica si la solicitud es de tipo POST
        required_fields = [  # Lista de campos requeridos para la creación del hotel
            "idhotel",
            "nombreestablecimiento",
            "horacheckin",
            "horacheckout",
            "petfriendly",
            "servicio",
            "numerointerior",
            "numeroexterior",
            "colonia",
            "calle",
            "estado"
        ]

        # Verifica que todos los campos requeridos están presentes en la solicitud POST
        for field in required_fields:
            if field not in request.POST:
                return HttpResponseBadRequest(f"Falta el campo '{field}'.")  # Devuelve un error si falta un campo

        # Crea un nuevo objeto Hotel con los datos de la solicitud POST
        nuevo_hotel = Hotel(
            idhotel=request.POST.get("idhotel"),  # Obtiene el valor del campo 'idHotel' del POST
            nombreestablecimiento=request.POST.get("nombreestablecimiento"),  # Obtiene el nombre del establecimiento
            horacheckin=request.POST.get("horacheckin"),  # Hora de check-in
            horacheckout=request.POST.get("horacheckout"),  # Hora de check-out
            petfriendly=request.POST.get("petfriendly"),  # Convierte el valor a booleano
            servicio=request.POST.get("servicio"),  # Obtiene el tipo de servicio
            numerointerior=request.POST.get("numerointerior"),  # Puede ser nulo, número de interior
            numeroexterior=int(request.POST.get("numeroexterior")),  # Convierte a entero, número de exterior
            colonia=request.POST.get("colonia"),  # Colonia
            calle=request.POST.get("calle"),  # Calle
            estado=request.POST.get("estado")  # Estado
        )

        # Guarda el nuevo objeto Hotel en la base de datos
        nuevo_hotel.save()

        # Redirige a la página principal después de guardar con éxito
        return redirect('/')  # Redirige a la página de inicio

    else:
        # Devuelve un error si la solicitud no es de tipo POST
        return HttpResponseBadRequest("Solo se aceptan solicitudes POST.")  # Solo acepta solicitudes POST



def deleteHotel(request, hotel_id):
    '''
    Elimina un hotel dado su identificador único.

    Esta función elimina un objeto 'Hotel' de la base de datos utilizando su identificador único
    proporcionado como argumento. Tras eliminar el hotel, redirige a la página de inicio.

    :param request: Una instancia de HttpRequest que representa la solicitud entrante desde el cliente.
    :param hotel_id: El identificador único del hotel que se desea eliminar.
    :return: Una respuesta HTTP que redirige a la página de inicio después de eliminar el hotel.
    '''
    hotel_deleted = Hotel.objects.get(idhotel=hotel_id)  # Obtiene el hotel a eliminar por su id
    hotel_deleted.delete()  # Elimina el objeto Hotel de la base de datos
    return redirect('/')  # Redirige a la página de inicio después de eliminar



def editHotelRender(request, hotel_id):
    '''
    Renderiza el formulario para editar un hotel.

    Esta función obtiene un objeto 'Hotel' de la base de datos utilizando su identificador único
    y lo pasa al contexto para renderizar la plantilla 'edicionHotel.html', donde se mostrará el
    formulario para editar los detalles del hotel.

    :param request: Una instancia de HttpRequest que representa la solicitud entrante desde el cliente.
    :param hotel_id: El identificador único del hotel que se desea editar.
    :return: Una respuesta HTTP que renderiza la plantilla 'edicionHotel.html' con el hotel a editar
             en el contexto.
    '''
    hotel_edited = Hotel.objects.get(idhotel=hotel_id)  # Obtiene el hotel a editar
    return render(request, "edicionHotel.html",
                  {"hotel_edited": hotel_edited})  # Renderiza la vista de edición con el hotel a editar



def editHotel(request, hotel_id):
    '''
    Actualiza la información de un hotel existente.

    Esta función obtiene un objeto 'Hotel' por su identificador único. Si el hotel existe,
    actualiza sus detalles con la información proporcionada en una solicitud POST.
    Si la solicitud no es de tipo POST, se devuelve un error.

    :param request: Una instancia de HttpRequest que representa la solicitud entrante desde el cliente.
    :param hotel_id: El identificador único del hotel que se desea editar.
    :return: Una respuesta HTTP que puede ser:
             - Redirección a la página principal tras actualizar con éxito.
             - HTTP 400 si la solicitud no es de tipo POST.
    '''
    hotel = get_object_or_404(Hotel, idhotel=hotel_id)  # Obtiene el objeto Hotel por su id, o retorna 404 si no existe

    if request.method == 'POST':  # Verifica si la solicitud es de tipo POST
        # Actualiza el objeto Hotel con nuevos datos obtenidos del POST
        hotel.nombreestablecimiento = request.POST.get("nombreestablecimiento")
        hotel.horacheckin = request.POST.get("horacheckin")
        hotel.horacheckout = request.POST.get("horacheckout")
        hotel.petfriendly = request.POST.get("petfriendly")   # Convierte a booleano
        hotel.servicio = request.POST.get("servicio")
        hotel.numerointerior = request.POST.get("numerointerior")
        hotel.numeroexterior = request.POST.get("numeroexterior")  # Convierte a entero
        hotel.colonia = request.POST.get("colonia")
        hotel.calle = request.POST.get("calle")
        hotel.estado = request.POST.get("estado")

        # Guarda los cambios en la base de datos
        hotel.save()

        # Redirige a la página principal después de editar con éxito
        return redirect('/')  # Redirige a la página de inicio

    else:
        # Devuelve un error si la solicitud no es de tipo POST
        return HttpResponseBadRequest("Solo se aceptan solicitudes POST.")  # Solo acepta solicitudes POST



def readHotelRender(request, hotel_id):
    '''
    Renderiza la vista de detalles de un hotel.

    Esta función obtiene un objeto 'Hotel' por su identificador único y lo pasa al contexto para
    renderizar la plantilla 'leerHotel.html', permitiendo mostrar la información del hotel
    seleccionado.

    :param request: Una instancia de HttpRequest que representa la solicitud entrante desde el cliente.
    :param hotel_id: El identificador único del hotel cuyos detalles se desean visualizar.
    :return: Una respuesta HTTP que renderiza la plantilla 'leerHotel.html' con el hotel a leer
             en el contexto.
    '''
    hotel_readed = Hotel.objects.get(idhotel=hotel_id)  # Obtiene el hotel a leer
    return render(request, "leerHotel.html",
                  {"hotel_readed": hotel_readed})  # Renderiza la vista con el hotel a leer



def readHotel(request, hotel_id):
    '''
    Lee y actualiza la información de un hotel existente.

    Esta función obtiene un objeto 'Hotel' por su identificador único. Si el método de la solicitud
    es POST, actualiza los detalles del hotel con los datos proporcionados en la solicitud.
    Si la solicitud no es de tipo POST, se devuelve un error.

    :param request: Una instancia de HttpRequest que representa la solicitud entrante desde el cliente.
    :param hotel_id: El identificador único del hotel cuyo detalle se quiere leer y posiblemente actualizar.
    :return: Una respuesta HTTP que puede ser:
             - Redirección a la página principal después de actualizar con éxito.
             - HTTP 400 si la solicitud no es de tipo POST.
    '''
    hotel = get_object_or_404(Hotel, idhotel=hotel_id)  # Obtiene el objeto Hotel por su id, o retorna 404 si no existe

    if request.method == 'POST':  # Verifica si la solicitud es de tipo POST
        # Actualiza el objeto Hotel con nuevos datos obtenidos del POST
        hotel.nombreEstablecimiento = request.POST.get("nombreEstablecimiento")
        hotel.horaCheckIn = request.POST.get("horaCheckIn")
        hotel.horaCheckOut = request.POST.get("horaCheckOut")
        hotel.petFriendly = request.POST.get("petFriendly") == 'on'  # Convierte a booleano
        hotel.servicio = request.POST.get("servicio")
        hotel.numeroInterior = request.POST.get("numeroInterior")
        hotel.numeroExterior = request.POST.get("numeroExterior")  # Convierte a entero
        hotel.colonia = request.POST.get("colonia")
        hotel.calle = request.POST.get("calle")
        hotel.estado = request.POST.get("estado")

        # Guarda los cambios en la base de datos
        hotel.save()

        # Redirige a la página principal después de editar con éxito
        return redirect('/')  # Redirige a la página de inicio

    else:
        # Devuelve un error si la solicitud no es de tipo POST
        return HttpResponseBadRequest("Solo se aceptan solicitudes POST.")  # Solo acepta solicitudes POST



def obtener_detalles_hotel(request, hotel_id):
    """
    Vista para obtener detalles de un hotel específico por su ID.

    Argumentos:
        request (HttpRequest): La solicitud HTTP que se está procesando.
        hotel_id (str): El ID del hotel para buscar en la base de datos.

    Retorno:
        JsonResponse: Datos del hotel en formato JSON. Contiene detalles del hotel
        como el ID, nombre, hora de check-in y check-out, si es pet-friendly,
        y ubicación.

    Excepciones:
        Http404: Se lanza si el hotel con el ID especificado no se encuentra.
    """
    # Obtiene el hotel por su ID, o devuelve 404 si no se encuentra
    hotel = get_object_or_404(Hotel, idhotel=hotel_id)

    # Estructura los datos para ser devueltos como JSON
    hotel_data = {
        'id': hotel.idhotel,
        'nombre_establecimiento': hotel.nombreestablecimiento,
        'hora_checkin': hotel.horacheckin,
        'hora_checkout': hotel.horacheckout,
        'pet_friendly': hotel.petfriendly,
        'servicios': hotel.servicio,
        'numero_interior': hotel.numerointerior,
        'numero_exterior': hotel.numeroexterior,
        'colonia': hotel.colonia,
        'calle': hotel.calle,
        'estado': hotel.estado,
    }

    return JsonResponse(hotel_data)  # Devuelve datos como JSON

