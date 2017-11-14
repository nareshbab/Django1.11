from django.contrib import admin
from .models import UserManager, User, Role, Group, Permission
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Group)
admin.site.register(Permission)