from django.contrib import admin

# Register your models here.
from django.contrib import admin

from author.models import MyUser

admin.site.register(MyUser)