"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppBlog.views import (
    inicio,
    equipos,
    jugadores,
    entrenadores,
    cargar_jugador,
    cargar_entrenador,
    cargar_equipo,
    busqueda_jugador,
    buscar_jugador,
    busqueda_entrenador,
    buscar_entrenador,
    busqueda_equipo,
    buscar_equipo,
    listar_equipos,
    Jugadorlist,
    JugadorDetail,
    JugadorCreate,
    JugadorUpdate,
    JugadorDelete,
    MyLogin,
    MyLogout,
    register,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("equipos", equipos, name="equipo"),
    path("jugadores", jugadores, name="jugador"),
    path("entrenadores", entrenadores, name="entrenador"),
    path("cargar-jugador", cargar_jugador, name="cargar-jugador"),
    path("cargar-entrenador", cargar_entrenador, name="cargar-entrenador"),
    path("cargar-equipo", cargar_equipo, name="cargar-equipo"),
    path("busqueda-jugador", busqueda_jugador, name="busqueda-jugador"),
    path("buscar-jugador", buscar_jugador, name="buscar-jugador"),
    path("busqueda-entrenador", busqueda_entrenador, name="busqueda-entrenador"),
    path("buscar-entrenador", buscar_entrenador, name="buscar-entrenador"),
    path("busqueda-equipo", busqueda_equipo, name="busqueda-equipo"),
    path("buscar-equipo", buscar_equipo, name="buscar-equipo"),
    path("listar-equipos", listar_equipos, name="listar-equipos"),
    path("jugador/list", Jugadorlist.as_view(), name="JugadorList"),
    path("r'(?P<pk>\d+)^$", JugadorDetail.as_view(), name="JugadorDetail"),
    path("jugador-nuevo", JugadorCreate.as_view(), name="JugadorCreate"),
    path("editar/<pk>", JugadorUpdate.as_view(), name="JugadorUpdate"),
    path("borrar/<pk>", JugadorDelete.as_view(), name="JugadorDelete"),
    path("login", MyLogin.as_view(), name="Login"),
    path("logout", MyLogout.as_view(), name="Logout"),
    path("register", register, name="register"),
]
