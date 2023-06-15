from django.contrib import admin

# Register your models here.

from .models import Post, Autor, Area, Account

admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Area)
admin.site.register(Account)