from django.db import models


class Payment(models.Model):
    course_name = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


from django.db import models


from django.db import models


from django.db import models


class CoursePayment(models.Model):
    course_name = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MachineLearningPayment(models.Model):
    course_name = models.CharField(max_length=50, default="Machine Learning Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


class FullStackPayment(models.Model):
    course_name = models.CharField(max_length=50, default="Full Stack Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


class FrontEndPayment(models.Model):
    course_name = models.CharField(max_length=50, default="Front End Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


class BackEndPayment(models.Model):
    course_name = models.CharField(max_length=50, default="Back End Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


class CCPayment(models.Model):
    course_name = models.CharField(max_length=50, default="C/C++ Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


class DataAnalyticsPayment(models.Model):
    course_name = models.CharField(max_length=50, default="Data Analytics Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"


class DataSciencePayment(models.Model):
    course_name = models.CharField(max_length=50, default="Data Science Course")
    transaction_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    account_holder = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    # pen= models.CharField(max_length=50,null=True,blank=True)
    pencil=models.IntegerField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"{self.name} - {self.course_name}"
