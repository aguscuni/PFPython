from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.forms import (
    JugadorFormulario,
    EntrenadorFormulario,
    EquipoFormulario,
    UserEditionForm,
    AvatarForm,
)
from AppBlog.models import Jugador, Entrenador, Equipo, Avatar
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inicio(request):
    return render(request, "AppBlog/inicio.html")


@login_required
def equipos(request):
    return render(request, "AppBlog/equipos.html")


@login_required
def jugadores(request):
    return render(request, "AppBlog/jugadores.html")


@login_required
def entrenadores(request):
    return render(request, "AppBlog/entrenadores.html")


@login_required
def cargar_jugador(request):
    if request.method != "POST":
        mi_formulario = JugadorFormulario()

    else:
        mi_formulario = JugadorFormulario(request.POST)
        if mi_formulario.is_valid():
            information = mi_formulario.cleaned_data
            jugador = Jugador(
                name=information["name"],
                surname=information["surname"],
                position=information["position"],
                country=information["country"],
                birth=information["birth"],
            )
            jugador.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppBlog/cargar_jugador.html", contexto)


@login_required
def cargar_entrenador(request):
    if request.method != "POST":
        mi_formulario = EntrenadorFormulario()

    else:
        mi_formulario = EntrenadorFormulario(request.POST)
        if mi_formulario.is_valid():
            information = mi_formulario.cleaned_data
            entrenador = Entrenador(
                name=information["name"],
                surname=information["surname"],
                country=information["country"],
                birth=information["birth"],
            )
            entrenador.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppBlog/cargar_entrenador.html", contexto)


@login_required
def cargar_equipo(request):
    if request.method != "POST":
        mi_formulario = EquipoFormulario()

    else:
        mi_formulario = EquipoFormulario(request.POST)
        if mi_formulario.is_valid():
            information = mi_formulario.cleaned_data
            equipo = Equipo(
                name=information["name"],
                country=information["country"],
                foundation_year=information["foundation_year"],
            )
            equipo.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppBlog/cargar_equipo.html", contexto)


@login_required
def busqueda_jugador(request):
    return render(request, "AppBlog/busqueda_jugador.html")


@login_required
def buscar_jugador(request):
    if not request.GET["jugador"]:
        return HttpResponse("No enviaste datos")

    else:
        jugador_a_buscar = request.GET["jugador"]
        jugadores = Jugador.objects.filter(
            surname=jugador_a_buscar
        ) or Jugador.objects.filter(country=jugador_a_buscar)

        contexto = {"jugador": jugador_a_buscar, "jugadores_encontrados": jugadores}

        return render(request, "AppBlog/resultado_busqueda_jugador.html", contexto)


@login_required
def busqueda_entrenador(request):
    return render(request, "AppBlog/busqueda_entrenador.html")


@login_required
def buscar_entrenador(request):
    if not request.GET["entrenador"]:
        return HttpResponse("No enviaste datos")

    else:
        entrenador_a_buscar = request.GET["entrenador"]
        entrenadores = Entrenador.objects.filter(
            surname=entrenador_a_buscar
        ) or Entrenador.objects.filter(country=entrenador_a_buscar)

        contexto = {
            "entrenador": entrenador_a_buscar,
            "entrenadores_encontrados": entrenadores,
        }

        return render(request, "AppBlog/resultado_busqueda_entrenador.html", contexto)


@login_required
def busqueda_equipo(request):
    return render(request, "AppBlog/busqueda_equipo.html")


@login_required
def buscar_equipo(request):
    if not request.GET["equipo"]:
        return HttpResponse("No enviaste datos")

    else:
        equipo_a_buscar = request.GET["equipo"]
        equipos = Equipo.objects.filter(name=equipo_a_buscar) or Equipo.objects.filter(
            country=equipo_a_buscar
        )

        contexto = {"equipo": equipo_a_buscar, "equipos_encontrados": equipos}

        return render(request, "AppBlog/resultado_busqueda_equipo.html", contexto)


@login_required
def listar_equipos(request):

    todos_los_equipos = Equipo.objects.all()

    contexto = {"equipos_encontrados": todos_los_equipos}

    return render(request, "AppBlog/listar_equipos.html", contexto)


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class Jugadorlist(LoginRequiredMixin, ListView):
    model = Jugador
    template_name = "AppBlog/jugadores_list.html"


class JugadorDetail(LoginRequiredMixin, DetailView):
    model = Jugador
    template_name = "AppBlog/jugadores_detalle.html"


class JugadorCreate(LoginRequiredMixin, CreateView):
    model = Jugador
    success_url = "/AppBlog/jugador/list"
    fields = ["name", "surname", "position", "country", "birth"]


class JugadorUpdate(LoginRequiredMixin, UpdateView):
    model = Jugador
    success_url = "/AppBlog/jugador/list"
    fields = ["name", "surname", "position", "country", "birth"]


class JugadorDelete(LoginRequiredMixin, DeleteView):
    model = Jugador
    success_url = "/AppBlog/jugador/list"


class MyLogin(LoginView):
    template_name = "AppBlog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "AppBlog/logout.html"


def register(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(
                request, "AppBlog/inicio.html", {"mensaje": f"Usuario {username}!"}
            )

    else:
        form = UserCreationForm()

    return render(request, "AppBlog/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user

    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"user": user, "form": form}
    return render(request, "AppBlog/editar_perfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"form": form}
    return render(request, "AppBlog/avatar_form.html", contexto)
