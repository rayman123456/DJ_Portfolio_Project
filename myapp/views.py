from django.shortcuts import render
from .models import Images
from django.core.mail import EmailMessage
from django.contrib import messages


def home(request):
    context = {}

    images = Images.objects.all()
    context["images"] = images

    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_message = EmailMessage(
            subject = name + " :" + subject,
            body= message,
            to= ['rehan.akaray98@gmail.com'],
            headers= {"Reply-To": email}
        )
        email_message.send()
        messages.success(request, "Thanks for the Email. We will get back to you shortly...")
        return render(request, "contact.html")
    else:



        return render(request, "index.html", context)
