from django.db import models
from django.contrib.auth.models import User

class ActivePeriodoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)

class Periodo(models.Model):
    periodo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    state = models.BooleanField('Activo', default=True)

    objects = models.Manager()
    active_periodos = ActivePeriodoManager()

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        ordering = ['periodo']
        indexes = [models.Index(fields=['periodo']),]

    def __str__(self):
        return self.periodo
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
    
    
    
    
class ActiveAsignaturaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Asignatura(models.Model):
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    objects = models.Manager()
    active_asignatura = ActiveAsignaturaManager()

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]

    def __str__(self):
        return self.description
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
    
    
    
class ActiveProfesorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Profesor(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    objects = models.Manager()
    active_profesor = ActiveProfesorManager()

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['nombre']
        indexes = [models.Index(fields=['nombre']),]

    def __str__(self):
        return self.nombre
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
    
    
    
class ActiveEstudianteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Estudiante(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    objects = models.Manager()
    active_estudiante = ActiveEstudianteManager()

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['nombre']
        indexes = [models.Index(fields=['nombre']),]

    def __str__(self):
        return self.nombre
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
    
    
    
    
class ActiveNotaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Nota(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT, related_name='profesor_detalles', verbose_name='Profesor')
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT, related_name='periodo_detalles', verbose_name='Periodo')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT, related_name='asignatura_detalles', verbose_name='Asignatura')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    objects = models.Manager()
    active_estudiante = ActiveNotaManager()
    
    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ['profesor']
        indexes = [models.Index(fields=['profesor']),]

    def __str__(self):
        return f"{self.id} - {self.profesor.nombre}"
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
    
    
    
class ActiveDetalleNotaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class DetalleNota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT, related_name='estudiant', verbose_name='Estudiante')
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE, related_name='detail', verbose_name='Nota')
    nota1 = models.DecimalField(default=None, max_digits=10, decimal_places=2, null=True, blank=True)
    nota2 = models.DecimalField(default=None, max_digits=10, decimal_places=2, null=True, blank=True)
    recuperacion = models.DecimalField(verbose_name='recuperacion', default=None, max_digits=10, decimal_places=2, null=True, blank=True)
    observacion = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    objects = models.Manager()
    active_estudiante = ActiveDetalleNotaManager()
    
    class Meta:
        verbose_name = "Nota Detalle"
        verbose_name_plural = "Nota Detalles"
        ordering = ['id']
        indexes = [models.Index(fields=['id']),]

    def __str__(self):
        return f"{self.estudiante}"
    
    def delete(self, *args, **kwargs):
        self.state = False
        self.save()


