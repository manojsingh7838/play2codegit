# Generated by Django 5.0.4 on 2024-09-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('account_holder', models.CharField(max_length=50)),
            ],
        ),
    ]
