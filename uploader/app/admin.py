from django.contrib import admin
from app.models import Arquivo, Midia, Upload

# Register your models here.
admin.site.register(Arquivo)
admin.site.register(Midia)
admin.site.register(Upload)