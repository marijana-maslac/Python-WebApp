from django.contrib import admin
from .models import Korisnici, Upisi,  Predmeti

# Register your models here.

admin.site.register(Korisnici)
admin.site.register(Upisi)
admin.site.register(Predmeti)
