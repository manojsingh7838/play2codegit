# onlinecompiler/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("doc", include("course.urls")),
    path("compiler/",include("compiler.urls")),
    path("account/",include("accounts.urls")),
    path("",include("home.urls")),
    path("ai/",include("p2cAI.urls")),
    path("payment/",include("payment.urls")),
    
]
