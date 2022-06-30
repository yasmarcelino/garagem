from django.contrib import admin

from core.models import Categoria

admin.site.register(Categoria)

from core.models import Marca

admin.site.register(Marca)