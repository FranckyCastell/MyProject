from django.conf import settings
from django.shortcuts import redirect, render
from .forms import Contact
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            username = request.user
            subject = f'{username} Tiene una Duda'
            message = 'Correo Electronico de: ' + request.user.email + \
                ' Mensaje: ' + request.POST['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['francesc.castell8@gmail.com']
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Su Mensaje se envió Correctamente')

            return redirect('contact')
    else:
        form = Contact()

    username = request.user
    email = request.user.email

    context = {'form': form, 'username': username, 'email': email}
    return render(request, 'Contact/contact.html', context)
