from django.contrib import admin

from .models import Curso
from .models import Directivo
from .models import Preceptor
from .models import Alumno
from .models import PadreTutor
from .models import Formulario
from .models import SolicitudReunion
from .models import ComunicadoCurso
from .models import ComunicadoCiclo
from .models import ComunicadoGeneral

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Curso, CursoAdmin)

class DirectivoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Directivo,DirectivoAdmin)

class PreceptorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Preceptor,PreceptorAdmin)

class AlumnoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Alumno,AlumnoAdmin)
class PadreTutorAdmin(admin.ModelAdmin):
    pass
admin.site.register(PadreTutor,PadreTutorAdmin)

class FormularioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Formulario,FormularioAdmin)

class SolicitudReunionAdmin(admin.ModelAdmin):
    pass

admin.site.register(SolicitudReunion,SolicitudReunionAdmin)

class ComunicadoCursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(ComunicadoCurso,ComunicadoCursoAdmin)

class ComunicadoCicloAdmin(admin.ModelAdmin):
    pass

admin.site.register(ComunicadoCiclo,ComunicadoCicloAdmin)

class ComunicadoGeneralAdmin(admin.ModelAdmin):
    pass
admin.site.register(ComunicadoGeneral,ComunicadoGeneralAdmin)
