from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'airbagfix_web/home.html', {}) # al mover los templates al folder templates dentro de 
# la aplicacion y asi mismo a una carpeta con el mismo nombre de la aplicacion, 
# solo basta con añandir nombre_de_la_app/pagina.html para renderizarlo

def airbag(request):
    return render(request, 'airbagfix_web/airbag.html', {})

def archivos(request):
    return render(request, 'airbagfix_web/archivos.html', {})

def dpf(request):
    return render(request, 'airbagfix_web/dpf.html', {})

def leer(request):
    return render(request, 'airbagfix_web/leer.html', {})

def contacts(request):
    # Ojo con el orden de los campor, ya que si se agregan mas campos habra error, Los unicos necesarios con estos 3
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Enviar email Poneren este ORDEN para que funcione correctamente:
        send_mail(
            message_name,
            message,
            message_email,
            ['info@airbagfix.mx'],
            fail_silently = 'True', # En produccion el valor es TRUE
            )
        
        return render(request, 'airbagfix_web/contacts.html', {'message_name' : message_name})

    else:
        return render(request, 'airbagfix_web/contacts.html', {}) 

