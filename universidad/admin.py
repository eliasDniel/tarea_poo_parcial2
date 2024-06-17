from django.contrib import admin

from universidad.models import Asignatura,Periodo,Profesor,Estudiante,Nota,DetalleNota

admin.site.register(Asignatura)
admin.site.register(Periodo)
admin.site.register(Estudiante)
admin.site.register(Nota)
admin.site.register(DetalleNota)


# Registra la clase ProductAdmin como administrador de los modelos de tipo Product en el panel de administración de Django
@admin.register(Profesor)
class PeriodoAdmin(admin.ModelAdmin):
    pass
    # Especifica los campos que se mostrarán en la lista de productos en el panel de administración
    # list_display = ['periodo','state']
    # # Define los campos por los cuales se pueden filtrar los productos en el panel de administración
    # list_filter = ['state', 'periodo']
    # # Especifica los campos por los cuales se puede buscar productos en el panel de administración
    # search_fields = ['periodo']
    # ordering = ['periodo']

    # # Define un método para mostrar las categorías de cada producto en la lista del panel de administración
    # def categorias(self, obj):
    #     # Devuelve una cadena que contiene las descripciones de todas las categorías asociadas al producto, separadas por un guion (-)
        # return " - ".join([c.periodo for c in obj.periodo.all().order_by('periodo')])