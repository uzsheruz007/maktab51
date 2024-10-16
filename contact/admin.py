from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from .models import User, Contact

admin.site.register([User, Contact])


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['surname','number', 'messages',]
#     search_fields = ['surname']
