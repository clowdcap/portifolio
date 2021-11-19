from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_pub']
    list_filter = ['titulo', 'autor']
    search_fields = ['titulo']