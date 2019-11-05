from django.contrib import admin
from django.contrib.auth.models import Group
from .models import blog,index
# Register your models here.
admin.site.register(blog)
admin.site.register(index)
admin.site.unregister(Group)
