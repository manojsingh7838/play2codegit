# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import (
    Payment,
    CoursePayment,
    MachineLearningPayment,
    FullStackPayment,
    FrontEndPayment,
    BackEndPayment,
    CCPayment,
    DataAnalyticsPayment,
    DataSciencePayment,
)


@login_required(login_url="/account/login/")  # Redirect to this URL if not logged in
def sql_payment_view(request):
    if request.method == "POST":
        course_name = request.POST.get("course-name")
        transaction_id = request.POST.get("transaction-id")
        name = request.POST.get("name")
        account_holder = request.POST.get("account-holder")

        payment = Payment(
            course_name=course_name,
            transaction_id=transaction_id,
            name=name,
            account_holder=account_holder,
        )
        payment.save()

        send_mail(
            "New Payment Received",
            f"Payment details:\n\nCourse Name: {course_name}\nTransaction ID: {transaction_id}\nName: {name}\nAccount Holder: {account_holder}",
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False,
        )
        return redirect("success")

    return render(request, "SQL.html")


@login_required(login_url="/account/login/")
def payment_view(request):
    if request.method == "POST":
        course_name = request.POST["course-name"]
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = CoursePayment.objects.create(
            course_name=course_name,
            transaction_id=transaction_id,
            name=name,
            account_holder=account_holder,
        )

        subject = "New Payment Received"
        message = f"""
        A new payment has been received.

        Course Name: {course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER, request.user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "python.html")


@login_required(login_url="/account/login/")
def machine_learning_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = MachineLearningPayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New Payment Received"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "ml.html")


@login_required(login_url="/account/login/")
def full_stack_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = FullStackPayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New Payment Received"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "FSD.html")


@login_required(login_url="/account/login/")
def front_end_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = FrontEndPayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New Front End Course Payment"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "FED.html")


@login_required(login_url="/account/login/")
def back_end_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = BackEndPayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New Back End Course Payment"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "BD.html")


@login_required(login_url="/account/login/")
def cc_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = CCPayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New C/C++ Course Payment"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "C.html")


@login_required(login_url="/account/login/")
def data_analytics_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = DataAnalyticsPayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New Data Analytics Course Payment"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "DA.html")


@login_required(login_url="/account/login/")
def data_science_payment(request):
    if request.method == "POST":
        transaction_id = request.POST["transaction-id"]
        name = request.POST["name"]
        account_holder = request.POST["account-holder"]

        payment = DataSciencePayment.objects.create(
            transaction_id=transaction_id, name=name, account_holder=account_holder
        )

        subject = "New Data Science Course Payment"
        message = f"""
        A new payment has been received.

        Course Name: {payment.course_name}
        Transaction ID: {transaction_id}
        Name: {name}
        Account Holder: {account_holder}
        """
        recipient_list = [settings.EMAIL_HOST_USER]
        if request.user.is_authenticated:
            recipient_list.append(request.user.email)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        return redirect("success")

    return render(request, "DS.html")
