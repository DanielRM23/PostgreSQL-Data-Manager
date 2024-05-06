from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Hotel

# Create your views here.


def list_tasks(request):
    Hotels = Hotel.objects.all()
    return render(request, "list_tasks.html", {'Hotels': Hotels})


# función que crea un hotel
def createHotel(request):
    if request.method == 'POST':
        # Todos los campos requeridos están presentes
        required_fields = [
            "idHotel",
            "nombreEstablecimiento",
            "horaCheckIn",
            "horaCheckOut",
            "petFriendly",
            "servicio",
            "numeroInterior",
            "numeroExterior",
            "colonia",
            "calle",
            "estado"
        ]

        # Verificar que todos los campos requeridos están presentes
        for field in required_fields:
            if field not in request.POST:
                return HttpResponseBadRequest(f"Falta el campo '{field}'.")

        # Crear un nuevo objeto Hotel con los valores del POST
        nuevo_hotel = Hotel(
            idHotel=request.POST.get("idHotel"),
            nombreEstablecimiento=request.POST.get("nombreEstablecimiento"),
            horaCheckIn=request.POST.get("horaCheckIn"),
            horaCheckOut=request.POST.get("horaCheckOut"),
            petFriendly=request.POST.get("petFriendly") == 'on',  # Convertir a booleano
            servicio=request.POST.get("servicio"),
            numeroInterior=request.POST.get("numeroInterior"),  # Puede ser None
            numeroExterior=int(request.POST.get("numeroExterior")),  # Convertir a entero
            colonia=request.POST.get("colonia"),
            calle=request.POST.get("calle"),
            estado=request.POST.get("estado")
        )

        # Guardar el objeto en la base de datos
        nuevo_hotel.save()

        # Redirigir después de guardar con éxito
        return redirect('/')

    else:
        # Manejo de solicitudes que no sean POST
        return HttpResponseBadRequest("Solo se aceptan solicitudes POST.")


def deleteHotel(request, hotel_id):
    hotel_deleted = Hotel.objects.get(idHotel=hotel_id)
    hotel_deleted.delete()
    return redirect('/')

def editHotelRender(request, hotel_id):
    hotel_edited = Hotel.objects.get(idHotel=hotel_id)
    return render(request, "edicionHotel.html", {"hotel_edited": hotel_edited})


def editHotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, idHotel=hotel_id)

    if request.method == 'POST':
        # Actualizar el objeto existente
        hotel.nombreEstablecimiento = request.POST.get("nombreEstablecimiento")
        hotel.horaCheckIn = request.POST.get("horaCheckIn")
        hotel.horaCheckOut = request.POST.get("horaCheckOut")
        hotel.petFriendly = request.POST.get("petFriendly") == 'on'
        hotel.servicio = request.POST.get("servicio")
        hotel.numeroInterior = request.POST.get("numeroInterior")
        hotel.numeroExterior = int(request.POST.get("numeroExterior"))
        hotel.colonia = request.POST.get("colonia")
        hotel.calle = request.POST.get("calle")
        hotel.estado = request.POST.get("estado")

        # Guardar cambios
        hotel.save()

        # Redirigir después de la edición
        return redirect('/')
    else:
        return HttpResponseBadRequest("Solo se aceptan solicitudes POST.")


