from django.db import models
import datetime

# Create your models here.
class Curso(models.Model):

    class Cursos(models.TextChoices):
        primeroA = '1A', _('Primero A')
        primeroB = '1B', _('Primero B')
        primeroC = '1C', _('Primero C')

        segundoA = '2A', _('Segundo A')
        segundoB = '2B', _('Segundo B')
        segundoC = '2C', _('Segundo C')

        terceroA = '3A', _('Tercero A')
        terceroB = '3B', _('Tercero B')
        terceroC = '3C', _('Tercero C')

        cuartoA = '4A', _('Cuarto A')
        cuartoB = '4B', _('Cuarto B')
        cuartoC = '4C', _('Cuarto C')

        quintoA = '5A', _('Quinto A')
        quintoB = '5B', _('Quinto B')
        quintoC = '5C', _('Quinto C')

        sextoA = '6A', _('Sexto A')
        sextoB = '6B', _('Sexto B')
        sextoC = '6C', _('Sexto C')

        septimoA = '7A', _('Septimo A')
        septimoB = '7B', _('Septimo B')
        septimoC = '7C', _('Septimo C')

    curso = models.CharField(max_length=2, choices=Cursos.choices, default=Cursos.primeroA,)

class Directivo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Preceptor(models.Model):
    curso = models.ManyToManyField(Curso, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)

class Comunicado(models.Model):
    fecha = models.dateField()
    remitente = models.CharField(max_length=30)
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE)
    mensaje = models.TextField()
    cursos = models.ManyToManyField(Curso)

class Alumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)

class PadreTutor(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    delegado = models.BooleanField(default=False)
