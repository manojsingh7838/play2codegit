from django.shortcuts import render


# Create your views here.
def homes(request):
    return render(request, "home.html")


def free(request):
    return render(request, "freelance.html")


def courses(request):
    return render(request, "course.html")


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactSubmission
from django.conf import settings


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save form data to the model
        contact = ContactSubmission.objects.create(
            name=name, email=email, phone=phone, subject=subject, message=message
        )

        # Compose the email content
        email_subject = f"New Contact Form Submission: {subject}"
        email_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        # Send the email
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],  # Send to your email
            fail_silently=False,
        )

        return redirect("/")  # Redirect to a success page after submission

    return render(request, "contact.html")


def profile_view(request):
    return render(request, "profile.html")
