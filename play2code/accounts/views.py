import random
import logging
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser, OTP
from .forms import UserRegistrationForm, OTPVerificationForm
from django.db import transaction
from django.utils.crypto import get_random_string

logger = logging.getLogger(__name__)


def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  
            user.save()
            otp_code = random.randint(100000, 999999)
            OTP.objects.create(user=user, otp=str(otp_code))

            # Send OTP via email
            send_mail(
                "Your OTP Code",
                f"Your OTP is {otp_code}.",
                "play2code@outlook.com",
                [user.email],
                fail_silently=False,
            )

            # Use a token instead of email in the URL
            token = get_random_string(length=32)
            user.otp_token = token
            user.save()

            return redirect(f"/account/otp-auth/?token={token}")
    else:
        form = UserRegistrationForm()
    return render(request, "signup.html", {"form": form})


def otp_verification_view(request):
    logger.debug("otp_verification_view called")

    token = request.GET.get("token")
    user = CustomUser.objects.filter(otp_token=token).first()

    if not user:
        logger.error("Invalid or expired OTP token.")
        return render(
            request, "otp_auth.html", {"error": "Invalid or expired OTP token."}
        )

    if request.method == "POST":
        form = OTPVerificationForm(request.POST)

        if form.is_valid():
            otp_entry = OTP.objects.filter(user=user).last()
            if not otp_entry:
                logger.error("No OTP found for the user.")
                return render(request, "otp_auth.html", {"error": "No OTP found."})

            entered_otp = form.cleaned_data["otp"]

            if str(entered_otp).strip() == str(otp_entry.otp).strip():
                if otp_entry.is_verified:
                    logger.info("OTP already verified.")
                    return render(
                        request, "otp_auth.html", {"error": "OTP already verified."}
                    )

                if not is_otp_valid(otp_entry):
                    logger.info("OTP has expired.")
                    return render(
                        request, "otp_auth.html", {"error": "OTP has expired."}
                    )

                try:
                    with transaction.atomic():
                        otp_entry.is_verified = True
                        otp_entry.save()
                        user.is_active = True
                        user.otp_token = None  
                        user.save()

                    logger.info("OTP verified successfully.")
                    print("OTP verified successfully.")
                    return redirect("account/login")
                except Exception as e:
                    logger.error(f"Error while verifying OTP or activating user: {e}")
                    return render(
                        request,
                        "otp_auth.html",
                        {"error": "An error occurred. Please try again."},
                    )
            else:
                logger.warning(f"Invalid OTP entered.")
                return render(request, "otp_auth.html", {"error": "Invalid OTP."})
    else:
        form = OTPVerificationForm()

    return render(request, "otp_auth.html", {"form": form})


def is_otp_valid(otp):
    expiry_time = otp.created_at + timedelta(hours=12)
    return timezone.now() <= expiry_time

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CustomUser  


def login_view(request):
    """
    Handle user login with custom user model.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print("Form is valid:", form.is_valid())  # Print form validity
        print("Form errors:", form.errors)  # Print form errors for debugging

        if form.is_valid():
            # Cleaned data
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    # Log the user in
                    auth_login(request, user)

                    return redirect(
                        "https://play2code.xyz/"
                    )  # Make sure 'home' is a valid URL pattern
                else:
                    messages.error(request, "Your account is inactive.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect


def logout_view(request):
    """
    Handles user logout.
    """
    logout(request)
    return redirect("/")


def home(request):
    return render(request, "home/home.html")
