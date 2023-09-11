from django.contrib import admin
from django.contrib import admin
from board.models import Board

# Register your models here.
@admin.register(Board)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("writer", "title", "post_date", "hit","down", "content")




