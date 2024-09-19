from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("sql/", sql_payment_view, name="payment"),
    path("python/", payment_view, name="payment"),
    path("ml/", machine_learning_payment, name="machine_learning_payment"),
    path("fsd/", full_stack_payment, name="full_stack_payment"),
    path("fed/", front_end_payment, name="front_end_payment"),
    path("backend/", back_end_payment, name="back_end_payment"),
    path("c/", cc_payment, name="cc_payment"),
    path("data-analytics/", data_analytics_payment, name="data_analytics_payment"),
    path("data-science/", data_science_payment, name="data_science_payment"),
]
