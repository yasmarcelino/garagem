from django.contrib import admin

from core.models import Marca, Modelos, Carro, Categoria

admin.site.register(Modelos)
admin.site.register(Marca)
admin.site.register(Carro)
admin.site.register(Categoria)

