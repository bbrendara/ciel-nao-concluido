from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
user = User.objects.create_user('cieladmin', 'escolaciel@hotmail.com', 'educacaoeachave')
user.is_staff = True
user.save()