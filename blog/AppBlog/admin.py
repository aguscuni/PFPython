from django.contrib import admin

from AppBlog.models import Equipo, Jugador, Entrenador, Avatar

# Register your models here.

admin.site.register(Equipo)

admin.site.register(Jugador)

admin.site.register(Entrenador)

admin.site.register(Avatar)
