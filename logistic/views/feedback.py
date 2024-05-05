import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
from django.core.mail import send_mail

def enviar_correo(request):
    if request.method == 'POST':
        cliente_email = request.POST.get('cliente_email')
        # Construir el cuerpo del correo electrónico
        mensaje = f"""
        Hola,

        Gracias por utilizar nuestro servicio logístico para tu evento. Nos encantaría conocer tu opinión sobre cómo fue tu experiencia.

        Por favor, responde a este correo electrónico con una puntuación del 1 al 5 y una breve descripción de tu experiencia. Tu retroalimentación es muy importante para nosotros.

        ¡Esperamos verte de nuevo pronto!

        Saludos,
        Equipo de apoyo logístico CCSA.
        """

        # Enviar el correo electrónico
        send_mail(
            'Calificación de servicio de apoyo logístico',  # Asunto del correo
            mensaje,  # Cuerpo del correo
            'apoyologisticoccsa@gmail.com',  # Correo electrónico remitente
            [cliente_email],  # Lista de destinatarios
            fail_silently=False,
        )

        return render(request, 'exito.html')  # Renderizar una página de éxito después de enviar el correo

    return render(request, 'formulario.html')  # Renderizar el formulario para capturar el correo del cliente
