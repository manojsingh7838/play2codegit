from django.contrib.auth.models import AbstractUser
from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    otp_token = models.CharField(max_length=32, blank=True, null=True)
    phoneno=models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        permissions = [
            ("can_view_customuser", "Can view custom user"),
        ]

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
    )


class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
