from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Payment)
admin.site.register(CoursePayment)
admin.site.register( MachineLearningPayment)
admin.site.register(FullStackPayment)
admin.site.register(FrontEndPayment)
admin.site.register(BackEndPayment)
admin.site.register(CCPayment)
admin.site.register(DataAnalyticsPayment)
admin.site.register(DataSciencePayment)
