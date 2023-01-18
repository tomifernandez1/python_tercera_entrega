from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Entregable, Estudiante

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):

      return render(request, "AppCoder/cursos.html")

def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")

from AppCoder.forms import CursoFormulario, ProfesorFormulario, EntregableFormulario, EstudianteFormulario

def cursoFormulario(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
            return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()
      return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})


def profesorFormulario(request):
      if request.method == "POST":
            miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre= informacion["nombre"], apellido =informacion["apellido"], email = informacion ["email"], profesion = informacion["profesion"])
                  profesor.save()
            return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = ProfesorFormulario()
      return render(request, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
      return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
      #respuesta = f"Estoy buscando la camada numero: {request.GET['camada']}"
      if request.GET["camada"]:
            camada= request.GET["camada"]
            cursos= Curso.objects.filter(camada__icontains=camada)
            return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})
      else:
            respuesta = "No enviaste datos"
      
      return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

def estudianteFormulario(request):
      if request.method == "POST":
            miFormulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante(nombre= informacion["nombre"], apellido =informacion["apellido"], email = informacion ["email"])
                  estudiante.save()
            return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EstudianteFormulario()
      return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario": miFormulario})     

 
def entregableFormulario(request):
      if request.method == "POST":
            miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  entregable = Entregable(nombre= informacion["nombre"],  fecha_de_entrega = informacion["fecha_de_entrega"], entregado = informacion ["entregado"])
                  entregable.save()
            return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EntregableFormulario()
      return render(request, "AppCoder/entregableFormulario.html", {"miFormulario": miFormulario})