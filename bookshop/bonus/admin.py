from django.contrib import admin
from .models import Client
from .models import BonusCard

admin.site.register(Client)
admin.site.register(BonusCard)