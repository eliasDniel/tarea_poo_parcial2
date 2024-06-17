
from datetime import date, datetime, timedelta
from decimal import Decimal
import os
import django
import random
from django.db.models.functions import Length,Coalesce
from django.db.models import F,Q ,Subquery, OuterRef, Exists,Count,FloatField, ExpressionWrapper,Sum,Max,Min,Avg
from django.forms import DecimalField

# Establece la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytareaPoo.settings')
# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from universidad.models import Asignatura,Nota,Profesor,Periodo,DetalleNota,Estudiante

def probar_orm():
    def script_periodos(create=False):
      if create:
        user= User.objects.get(username='admin')
        Periodo.objects.bulk_create([
          Periodo(periodo='2011-2011',user=user),
        Periodo(periodo='2011-2012',user=user),
        Periodo(periodo='2012-2013',user=user),
        Periodo(periodo='2013-2014',user=user),
        Periodo(periodo='2014-2015',user=user),
        Periodo(periodo='2015-2016',user=user),
        Periodo(periodo='2016-2017',user=user),
        Periodo(periodo='2017-2018',user=user),
        Periodo(periodo='2018-2019',user=user),
        Periodo(periodo='2019-2020',user=user)
        ])
    #2. Insertar 10 registros en la tabla Asignatura: Crear 10 asignaturas diferentes.
    def script_asignatura(create=False):
      if create:
        user= User.objects.get(username='admin')
        Asignatura.objects.bulk_create([
            Asignatura(description='Matematicas',user=user),
        Asignatura(description='Biologia',user=user),
        Asignatura(description='Quimica',user=user),
        Asignatura(description='Fisica',user=user),
        Asignatura(description='Historia',user=user),
        Asignatura(description='Ciudadania',user=user),
        Asignatura(description='Lengua y Literatura',user=user),
        Asignatura(description='Cultura Fisica',user=user),
        Asignatura(description='Educacion Artistica',user=user),
        Asignatura(description='Ingles',user=user),
        Asignatura(description='Programacion',user=user)
        ])
    #3. Insertar 10 registros en la tabla Estudiante: Crear 10 Estudiantes diferentes.
    def script_estudiante(create=False):
      if create:
        user= User.objects.get(username='admin')
        Estudiante.objects.bulk_create([
        Estudiante(cedula='0955026251',nombre='Esther',user=user),
        Estudiante(cedula='0943411835',nombre='Keyla',user=user),
        Estudiante(cedula='0912345678',nombre='Jenniffer',user=user),
        Estudiante(cedula='0987456321',nombre='Domenica',user=user),
        Estudiante(cedula='0931648975',nombre='Orlando',user=user),
        Estudiante(cedula='0954678932',nombre='Ariana',user=user),
        Estudiante(cedula='0096871366',nombre='Hortencia',user=user),
        Estudiante(cedula='0906246129',nombre='Estefanias',user=user),
        Estudiante(cedula='0955026252',nombre='David',user=user),
        Estudiante(cedula='0922335278',nombre='Maria',user=user),
        ])
    #4. Insertar 10 registros en la tabla Profesor: Crear 10 Profesores diferentes.
    def script_profesor(create=False):
        if create:
            user = User.objects.get(username='admin')
            Profesor.objects.bulk_create([
              Profesor(cedula='0923456789', nombre='Carlos', user=user),
            Profesor(cedula='0912345671', nombre='Andrea', user=user),
            Profesor(cedula='0912345672', nombre='Luis', user=user),
            Profesor(cedula='0912345673', nombre='Martha', user=user),
            Profesor(cedula='0912345674', nombre='Pedro', user=user),
            Profesor(cedula='0912345675', nombre='Ana', user=user),
            Profesor(cedula='0912345676', nombre='Hortencia', user=user),
            Profesor(cedula='0912345677', nombre='Sofia', user=user),
            Profesor(cedula='0912345678', nombre='Jose', user=user),
            Profesor(cedula='0912345679', nombre='Lucia', user=user),
            ])
    #.Create() y .save()
    #Insertar 10 registros en la tabla Nota: Registrar 10 notas vinculadas a los
    #periodos, profesores y asignaturas.
    def script_nota(create=False):
      if create:
        user=User.objects.first()
        profesores=Profesor.objects.all()
        asignaturas=Asignatura.objects.all()
        periodos=Periodo.objects.all()
        for nota in range(10):
          nota = Nota.objects.create(user=user,profesor=profesores[nota],asignatura=asignaturas[nota],periodo=periodos[nota])
          nota.save()
    #6. Insertar 10 registros en la tabla DetalleNota: Registrar los detalles de las
    #notas para 10 estudiantes de la opción 5
    def script_detalle_nota(create=False):
      if create:
        user=User.objects.first()
        estudiantes=Estudiante.objects.all()
        notas=Nota.objects.all()

        for estudiante in range(10):
          detalle_nota = DetalleNota.objects.create(
            user=user,
            estudiante=estudiantes[estudiante],
            nota=notas[estudiante],
            nota1=random.uniform(0,15),
            nota2=random.uniform(0,15),
            recuperacion=random.uniform(0,15),
            observacion='Se califico correctamente'
            )
          detalle_nota.save()

    
    def consultas_basicas():
        # 1. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est':
        filtro_estudiantes = Estudiante.active_estudiante.filter(nombre__startswith="Est")
        print('1. Seleccionar todos los estudiantes cuyo nombre comienza con Est:')
        if filtro_estudiantes.exists():
            for estudiante in filtro_estudiantes:
                print(f'Nombre: {estudiante.nombre}')
        else:
            print('No se encontraron estudiantes.')

        # 2. Seleccionar todos los profesores cuyo nombre contiene 'or':
        filtro_profesores = Profesor.active_profesor.filter(nombre__icontains="or")
        print('2. Seleccionar todos los profesores cuyo nombre contiene "or":')
        if filtro_profesores.exists():
            for profesor in filtro_profesores:
                print(f'Nombre: {profesor.nombre}')
        else:
            print('No se encontraron profesores.')

        # 3. Seleccionar todas las asignaturas cuya descripción termina en 'as':
        filtro_asignaturas = Asignatura.objects.filter(description__endswith="as")
        print('3. Seleccionar todas las asignaturas cuya descripción termina en "as":')
        if filtro_asignaturas.exists():
            for asignatura in filtro_asignaturas:
                print(f'Descripción: {asignatura.description}')
        else:
            print('No se encontraron asignaturas.')

        # 4. Seleccionar todas las notas con nota1 mayor que 8.0:
        filtro_notas_nota1 = DetalleNota.objects.filter(nota1__gt=8.0)
        print('4. Seleccionar todas las notas con nota1 mayor que 8.0:')
        if filtro_notas_nota1.exists():
            for nota in filtro_notas_nota1:
                print(f'Nota1: {nota.nota1}')
        else:
            print('No se encontraron notas con nota1 mayor que 8.0.')

        # 5. Seleccionar todas las notas con nota2 menor que 9.0:
        filtro_notas_nota2 = DetalleNota.objects.filter(nota2__lt=9.0)
        print('5. Seleccionar todas las notas con nota2 menor que 9.0:')
        if filtro_notas_nota2.exists():
            for nota in filtro_notas_nota2:
                print(f'Nota2: {nota.nota2}')
        else:
            print('No se encontraron notas con nota2 menor que 9.0.')

        # 6. Seleccionar todas las notas con recuperacion igual a 9.5:
        filtro_notas_recuperacion = DetalleNota.objects.filter(recuperacion=9.5)
        print('6. Seleccionar todas las notas con recuperacion igual a 9.5:')
        if filtro_notas_recuperacion.exists():
            for nota in filtro_notas_recuperacion:
                print(f'Recuperación: {nota.recuperacion}')
        else:
            print('No se encontraron notas con recuperación igual a 9.5.')

    #Consultas usando condiciones lógicas (AND, OR, NOT)
    def condiciones_logicas():
      # 7. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est' y su cedula termina en '1':
      print('7. Seleccionar todos los estudiantes cuyo nombre comienza con Est y su cedula termina en 1')
      estudiantes_filtrados = Estudiante.objects.filter(Q(nombre__startswith="Est") & Q(cedula__endswith="1"))
      if estudiantes_filtrados.exists():
          for estudiante in estudiantes_filtrados:
              print(f'Nombre: {estudiante.nombre}, Cédula: {estudiante.cedula}')
      else:
          print('No se encontraron estudiantes que cumplan con los criterios.')
      # 8. Seleccionar todas las asignaturas cuya descripción contiene 'Asig' o termina en '5':
      print('8. Seleccionar todas las asignaturas cuya descripción contiene Asig o termina en 5')
      asignaturas_filtradas = Asignatura.objects.filter(Q(description__contains="te") | Q(description__endswith="as"))
      if asignaturas_filtradas.exists():
          for asignatura in asignaturas_filtradas:
              print(f'Descripción: {asignatura.description}')
      else:
          print('No se encontraron asignaturas que cumplan con los criterios.')
      # 9. Seleccionar todos los profesores cuyo nombre no contiene 'or':
      print('9. Seleccionar todos los profesores cuyo nombre no contiene or')
      profesores_filtrados = Profesor.objects.filter(~Q(nombre__contains="or"))
      if profesores_filtrados.exists():
          for profesor in profesores_filtrados:
              print(f'Nombre: {profesor.nombre}')
      else:
          print('No se encontraron profesores que cumplan con los criterios.')

      # 10. Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0:
      print('10. Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0')
      notas_filtradas = DetalleNota.objects.filter(Q(nota1__gt=7.0) & Q(nota2__lt=8.0))
      if notas_filtradas.exists():
          for nota in notas_filtradas:
              print(f'Nota1: {nota.nota1}, Nota2: {nota.nota2}')
      else:
          print('No se encontraron notas que cumplan con los criterios.')

      # 11. Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0:
      print('11. Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0')
      notas_recuperacion_filtradas = DetalleNota.objects.filter(Q(recuperacion__isnull=True) | Q(nota2__gt=9.0))
      if notas_recuperacion_filtradas.exists():
          for nota in notas_recuperacion_filtradas:
              print(f'Recuperación: {nota.recuperacion}, Nota2: {nota.nota2}')
      else:
          print('No se encontraron notas que cumplan con los criterios.')
    def funciones_numericas():
      # 12. Seleccionar todas las notas con nota1 entre 7.0 y 9.0
      print('12. Seleccionar todas las notas con nota1 entre 7.0 y 9.0')
      notas_nota1_entre = DetalleNota.objects.filter(nota1__range=(7.0, 9.0))
      if notas_nota1_entre.exists():
          for nota in notas_nota1_entre:
              print(f'Nota1: {nota.nota1}')
      else:
          print('No se encontraron notas con nota1 entre 7.0 y 9.0')

      # 13. Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0
      print('13. Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0')
      notas_nota2_fuera_del_rango = DetalleNota.objects.filter(Q(nota2__lt=6.0) | Q(nota2__gt=8.0))
      if notas_nota2_fuera_del_rango.exists():
          for nota in notas_nota2_fuera_del_rango:
              print(f'Nota2: {nota.nota2}')
      else:
          print('No se encontraron notas con nota2 fuera del rango 6.0 a 8.0')

      # 14. Todas las notas cuya recuperacion no sea None
      print('14. Todas las notas cuya recuperacion no sea None')
      notas_recuperacion_not_null = DetalleNota.objects.exclude(recuperacion=None)
      if notas_recuperacion_not_null.exists():
          for nota in notas_recuperacion_not_null:
              print(f'Recuperación: {nota.recuperacion}')
      else:
          print('No se encontraron notas con recuperación distinta de None')
    
    def consultas_fechas():
        today = date.today()

        # 15. Seleccionar todas las notas creadas en el último año
        print('15. Seleccionar todas las notas creadas en el último año')
        notas_ultimo_año = DetalleNota.objects.filter(created__year=today.year)
        if notas_ultimo_año.exists():
            for nota in notas_ultimo_año:
                print(f'Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
        else:
            print('No se encontraron notas creadas en el último año.')

        # 16. Seleccionar todas las notas creadas en el último mes
        print('16. Seleccionar todas las notas creadas en el último mes')
        primer_dia_mes_actual = today.replace(day=1)
        ultimo_mes_pasado = primer_dia_mes_actual - timedelta(days=1)
        notas_ultimo_mes = DetalleNota.objects.filter(created__month=ultimo_mes_pasado.month, created__year=ultimo_mes_pasado.year)
        if notas_ultimo_mes.exists():
            for nota in notas_ultimo_mes:
                print(f'Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
        else:
            print('No se encontraron notas creadas en el último mes.')

        # 17. Seleccionar todas las notas creadas en el último día
        print('17. Seleccionar todas las notas creadas en el último día')
        notas_ultimo_dia = DetalleNota.objects.filter(created__date=today)
        if notas_ultimo_dia.exists():
            for nota in notas_ultimo_dia:
                print(f'Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
        else:
            print('No se encontraron notas creadas en el último día.')

        # 18. Seleccionar todas las notas creadas antes del año 2023
        print('18. Seleccionar todas las notas creadas antes del año 2023')
        notas_antes_2023 = DetalleNota.objects.filter(created__lt=date(2023, 1, 1))
        if notas_antes_2023.exists():
            for nota in notas_antes_2023:
                print(f'Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
        else:
            print('No se encontraron notas creadas antes del año 2023.')

        # 19. Seleccionar todas las notas creadas en marzo de cualquier año
        print('19. Seleccionar todas las notas creadas en marzo de cualquier año')
        notas_marzo = DetalleNota.objects.filter(created__month=3)
        if notas_marzo.exists():
            for nota in notas_marzo:
                print(f'Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
        else:
            print('No se encontraron notas creadas en marzo de cualquier año.')
    def consultas_combinadas():
      print('20. Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10 caracteres')
      estudiantes_con_nombre_de_10_caracteres = Estudiante.objects.filter(nombre__regex=r'^.{10}$')
      if estudiantes_con_nombre_de_10_caracteres.exists():
          for estudiante in estudiantes_con_nombre_de_10_caracteres:
              print(estudiante.nombre)
      else:
          print('No se encontraron estudiantes con nombre exactamente de 10 caracteres.')

      print('21. Seleccionar todas las notas con nota1 y nota2 mayores a 7.5')
      notas_mayores = DetalleNota.objects.filter(
          Q(nota1__gt=7.5) & Q(nota2__gt=7.5)
      )
      if notas_mayores.exists():
          for nota in notas_mayores:
              print(f"Nota1: {nota.nota1}, Nota2: {nota.nota2}")
      else:
          print('No se encontraron notas con nota1 y nota2 mayores a 7.5.')

      print('22. Seleccionar todas las notas con recuperacion no nula y nota1 mayor a nota2')
      notas_filtradas = DetalleNota.objects.filter(~Q(recuperacion__isnull=True) & Q(nota1__gt=F('nota2')))
      if notas_filtradas.exists():
          for nota in notas_filtradas:
              print(f"Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}")
      else:
          print('No se encontraron notas con recuperación no nula y nota1 mayor a nota2.')

      print('23. Seleccionar todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5')
      notas_filtradas = DetalleNota.objects.filter(
          Q(nota1__gt=8.0) | Q(nota2=7.5)
      )
      if notas_filtradas.exists():
          for nota in notas_filtradas:
              print(f"Nota1: {nota.nota1}, Nota2: {nota.nota2}")
      else:
          print('No se encontraron notas con nota1 mayor a 8.0 o nota2 igual a 7.5.')

      print('24. Seleccionar todas las notas con recuperacion mayor a nota1 y nota2')
      notas_filtradas = DetalleNota.objects.filter(
          Q(recuperacion__gt=F('nota1')) & Q(recuperacion__gt=F('nota2'))
      )
      if notas_filtradas.exists():
          for nota in notas_filtradas:
              print(f"Recuperación: {nota.recuperacion}, Nota1: {nota.nota1}, Nota2: {nota.nota2}")
      else:
          print('No se encontraron notas con recuperación mayor a nota1 y nota2.') 
    def subconsultas_anotaciones():
      print('25. Seleccionar todos los estudiantes con al menos una nota de recuperación')
      subquery = DetalleNota.objects.filter(
          estudiante_id=OuterRef('pk'),
          recuperacion__isnull=False
      )

      estudiantes_con_recuperacion = Estudiante.objects.filter(
          Exists(subquery)
      )

      if estudiantes_con_recuperacion.exists():
          for estudiante in estudiantes_con_recuperacion:
              print(f'Estudiante: {estudiante.nombre}, ID: {estudiante.id}')
      else:
          print('No se encontraron estudiantes con al menos una nota de recuperación.')

      print('26. Seleccionar todos los profesores que han dado una asignatura específica')
      asignatura_especifica = Asignatura.objects.get(pk=44)
      profesores = Profesor.objects.filter(profesor_detalles__asignatura=asignatura_especifica).distinct()

      if profesores.exists():
          for profesor in profesores:
              print(f'{profesor.nombre}: {asignatura_especifica.description}')
      else:
          print('No se encontraron profesores que hayan dado la asignatura específica.')

      print('27. Seleccionar todas las asignaturas que tienen al menos una nota registrada')
      asignaturas_con_al_menos = Asignatura.objects.filter(asignatura_detalles__isnull=False).distinct()

      if asignaturas_con_al_menos.exists():
          print('Asignaturas que tienen al menos una nota registrada:')
          for asignatura in asignaturas_con_al_menos:
              print(f'{asignatura.description}')
      else:
          print('No se encontraron asignaturas con al menos una nota registrada.')

      print('28. Seleccionar todas las asignaturas que no tienen notas registradas')
      asignaturas_sin_notas = Asignatura.objects.annotate(num_notas=Count('asignatura_detalles')).filter(num_notas=0)

      if asignaturas_sin_notas.exists():
          for asignatura in asignaturas_sin_notas:
              print(asignatura.description)
      else:
          print('Todas las asignaturas tienen al menos una nota registrada.')

      print('29. Seleccionar todos los estudiantes que no tienen notas de recuperación')
      estudiantes_sin_nota_recuperacion = Estudiante.objects.exclude(
          estudiant__recuperacion__isnull=False
      )

      if estudiantes_sin_nota_recuperacion.exists():
          print('Estudiantes que no tienen notas de recuperación:')
          for estudiante in estudiantes_sin_nota_recuperacion:
              print(estudiante.nombre)
      else:
          print('No se encontraron estudiantes sin notas de recuperación.')

      print('30. Seleccionar todas las notas cuyo promedio de nota1 y nota2 es mayor a 8.0')
      promedio_notas_expr = ExpressionWrapper(
          (F('nota1') + F('nota2')) / 2.0,
          output_field=FloatField()
      )

      notas_mayor_promedio = DetalleNota.objects.annotate(
          promedio_notas=promedio_notas_expr
      ).filter(
          promedio_notas__gt=8.0
      )

      if notas_mayor_promedio.exists():
          for nota in notas_mayor_promedio:
              print(f'Nota ID: {nota.id}, Promedio de Notas: {nota.promedio_notas}')
      else:
          print('No se encontraron notas con promedio de nota1 y nota2 mayor a 8.0.')

      print('31. Seleccionar todas las notas con nota1 menor que 6.0 y nota2 mayor que 7.0')
      notas_especificas = DetalleNota.objects.filter(
          Q(nota1__lt=6.0) & Q(nota2__gt=7.0)
      )

      if notas_especificas.exists():
          for nota in notas_especificas:
              print(f'Nota ID: {nota.id}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')
      else:
          print('No se encontraron notas con nota1 menor que 6.0 y nota2 mayor que 7.0.')

      print('32. Seleccionar todas las notas con nota1 en la lista [7.0, 8.0, 9.0]:')
      notas_a_seleccionar = [7.0, 8.0, 9.0]
      notas_seleccionadas = DetalleNota.objects.filter(nota1__in=notas_a_seleccionar)

      if notas_seleccionadas.exists():
          for nota in notas_seleccionadas:
              print(f'Nota ID: {nota.id}, Nota1: {nota.nota1}, Nota2: {nota.nota2}')
      else:
          print('No se encontraron notas con nota1 en la lista [7.0, 8.0, 9.0].')

      print('33. Seleccionar todas las notas cuyo id está en un rango del 1 al 5')
      notas_en_rango = DetalleNota.objects.filter(id__range=(1, 5))

      if notas_en_rango.exists():
          for nota in notas_en_rango:
              print(f'Nota ID: {nota.id}, Profesor: {nota.profesor}')
      else:
          print('No se encontraron notas con id en el rango del 1 al 5.')

      print('34. Seleccionar todas las notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]:')
      notas_excluidas = [8.0, 9.0, 10.0]
      notas_cuyo_recuperacion = DetalleNota.objects.exclude(recuperacion__in=notas_excluidas)

      if notas_cuyo_recuperacion.exists():
          for nota in notas_cuyo_recuperacion:
              print(f'Nota ID: {nota.id}')
      else:
          print('No se encontraron notas cuyo recuperación no está en la lista [8.0, 9.0, 10.0].')

      print('35. Suma de todas las notas de un estudiante')
      suma_notas_por_estudiante = DetalleNota.objects.annotate(
          total=F('nota1') + F('nota2') + F('recuperacion')
      ).aggregate(
          sumtotal=Sum('total', output_field=FloatField())
      )

      if suma_notas_por_estudiante['sumtotal'] is not None:
          print(f'Suma total de todas las notas: {suma_notas_por_estudiante["sumtotal"]}')
      else:
          print('No hay notas registradas para calcular la suma total.')

      print('36. Nota máxima obtenida por un estudiante')
      notas_maximas_por_estudiante = DetalleNota.objects.values('estudiante').annotate(
          max_nota=Max('nota1'), 
          max_nota2=Max('nota2'), 
          max_recuperacion=Max('recuperacion')
      )

      if notas_maximas_por_estudiante.exists():
          for nota in notas_maximas_por_estudiante:
              estudiante = Estudiante.objects.get(id=nota['estudiante'])
              nota_maxima = max(nota['max_nota'], nota['max_nota2'], nota['max_recuperacion'])
              print(f'Estudiante: {estudiante.nombre}, Nota máxima: {nota_maxima}')
      else:
          print('No se encontraron notas para calcular la nota máxima por estudiante.')

      print('37. Nota mínima obtenida por un estudiante')
      notas_minimas_por_estudiante = DetalleNota.objects.values('estudiante').annotate(
          min_nota=Min('nota1'), 
          min_nota2=Min('nota2'), 
          min_recuperacion=Min('recuperacion')
      )

      if notas_minimas_por_estudiante.exists():
          for nota in notas_minimas_por_estudiante:
              estudiante = Estudiante.objects.get(id=nota['estudiante'])
              nota_minima = min(nota['min_nota'], nota['min_nota2'], nota['min_recuperacion'])
              print(f'Estudiante: {estudiante.nombre}, Nota mínima: {nota_minima}')
      else:
          print('No se encontraron notas para calcular la nota mínima por estudiante.')

      print('38. Contar el número total de notas de un estudiante')
      total_notas_por_estudiante = DetalleNota.objects.values('estudiante').annotate(
          total_notas=(Count('nota1')+Count('nota2')+Count('recuperacion'))
      )
      

      if total_notas_por_estudiante.exists():
          for total in total_notas_por_estudiante:
              estudiante = Estudiante.objects.get(id=total['estudiante'])
              print(f'Estudiante: {estudiante.nombre}, Total de notas: {total["total_notas"]}')
      else:
          print('No se encontraron notas para calcular el total de notas por estudiante.')

      print('39. Promedio de todas las notas')
    def consultas_modelos_relacionados():
      print('40. Dado un estudiante obtener todas sus notas con el detalle de todos sus datos relacionados')   
      estudiante = Estudiante.objects.get(id=71)
      # Consulta para obtener todas las notas con el detalle de datos relacionados del estudiante
      notas_del_estudiante = DetalleNota.objects.filter(estudiante=estudiante)
      # Iterar sobre las notas y mostrar todos los detalles relacionados
      for nota in notas_del_estudiante:
          print(f'Estudiante: {nota.estudiante.nombre}')
          print(f'Nota: {nota}')
          print(f'Nota1: {nota.nota1}')
          print(f'Nota2: {nota.nota2}')
          print(f'Recuperación: {nota.recuperacion}')
          print(f'Observación: {nota.observacion}')
          print(f'Usuario: {nota.user.username}')
          print(f'Fecha de creación: {nota.created}')
          print(f'Fecha de actualización: {nota.updated}')
          print('---')
          
      print('41. Obtener todas las notas de un período específico')
      periodo_id = 1
      notas = Nota.active_estudiante.filter(periodo_id=periodo_id)
      
      if notas.exists():
          for nota in notas:
              print(f'Nota ID: {nota.id}, Profesor: {nota.profesor.nombre}, Asignatura: {nota.asignatura.description}')
      else:
          print('No se encontraron notas para el período específico.')
          
      print("42. Consultar todas las notas de una asignatura dada en un período:")
      asignatura_id = 48
      periodo_id = 52
      notas = Nota.active_estudiante.filter(asignatura_id=asignatura_id, periodo_id=periodo_id)
      if notas.exists():
          for nota in notas:
            print(f'Nota ID: {nota.id}, Profesor: {nota.profesor.nombre}, Asignatura: {nota.asignatura.description}')
      else:
          print('No se encontraron notas para la asignatura y período específicos.')
          
      print("43. Obtener todas las notas de un profesor en particular:")
      profesor_id = 1
      notas = Nota.active_estudiante.filter(profesor_id=profesor_id)
      if notas.exists():
          for nota in notas:
              print(f'Nota ID: {nota.id}, Profesor: {nota.profesor.nombre}, Asignatura: {nota.asignatura.description}')
      else:
          print('No se encontraron notas para el profesor especificado.')
          
      print("45. Obtener todas las notas de un estudiante ordenadas por período:")
      estudiante_id = 1
      notas = DetalleNota.active_estudiante.filter(estudiante_id=estudiante_id, state=True).order_by('nota__periodo')
      if notas.exists():
          for nota in notas:
              print(f'Estudiante: {nota.estudiante.nombre}, Período: {nota.nota.periodo.periodo}, Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
      else:
          print('No se encontraron notas para el estudiante especificado.')
          
          
      print('46. Consultar la cantidad total de notas para un estudiante')
      estudiante_id = 76
      total = DetalleNota.active_estudiante.filter(estudiante_id=estudiante_id, state=True).count()
      if total > 0:
          print(f'El total de notas para el estudiante {estudiante_id} es {total}')
      else:
          print(f'No se encontraron notas para el estudiante {estudiante_id}.')
          
      print('47. Calcular el promedio de las notas de un estudiante en un período dado')
      periodo_id = 53
      estudiante_id = 74
      promedio = DetalleNota.active_estudiante.filter(
          estudiante__id=estudiante_id, 
          nota__periodo__id=periodo_id, 
          state=True
      ).aggregate(promedio=Avg('nota1'))['promedio']
      
      if promedio is not None:
          print(f'El promedio de las notas del estudiante {estudiante_id} en el período {periodo_id} es {promedio}')
      else:
          print(f'No se encontraron notas para el estudiante {estudiante_id} en el período {periodo_id}')
          
          
      print('48. Consultar todas las notas sin una observación específica')
      observacion = 'Se calificó correctamente'
      # Assuming DetalleNota is a Django model representing student grades
      notas = DetalleNota.objects.exclude(observacion__icontains=observacion, state=True)
      if notas.exists():
          for nota in notas:
            print(f'Estudiante: {nota.estudiante.nombre}, Observación: {nota.observacion}, Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
      else:
          print(f'No se encontraron notas con la observación "{observacion}" y estado activo.')
          
      print('49. Obtener todas las notas de un estudiante ordenadas por asignatura')
      # Suponiendo que tienes definida la variable estudiante_id con el id del estudiante deseado
      estudiante_id = 77 # Aquí debes asignar el id del estudiante específico
      # Filtrar notas activas del estudiante ordenadas por asignatura
      notas = DetalleNota.objects.filter(estudiante_id=estudiante_id, state=True).order_by('nota__asignatura__description')
      # Verificar si hay notas para el estudiante
      if notas.exists():
          for nota in notas:
              print(f'Estudiante: {nota.estudiante.nombre}, Asignatura: {nota.nota.asignatura.description}, Nota1: {nota.nota1}, Nota2: {nota.nota2}, Recuperación: {nota.recuperacion}')
      else:
          print(f'No se encontraron notas para el estudiante con ID {estudiante_id} y estado activo.')    
    def sentencias_update():
        print('50. Actualizar nota1 para alumnos con nota1 < 20')
        condition=20
        DetalleNota.active_estudiante.filter(state=True, nota1__lt=condition).update(nota1=20)
        print(f'Se han actualizado las notas1 para estudiantes con nota1 < {condition}.')  
        
        
        
        print('51. Actualizar nota2 para alumnos con nota2 < 15')
        condition=15
        DetalleNota.active_estudiante.filter(state=True, nota2__lt=condition).update(nota2=15)
        print(f'Se han actualizado las notas2 para estudiantes con 2 < {condition}.')
        
        
        
        print('52. Actualizar recuperación para alumnos con recuperación < 10')
        condition=10
        DetalleNota.active_estudiante.filter(state=True, recuperacion__lt=condition).update(recuperacion=10)
        print(f'Se han actualizado las recuperaciones para estudiantes con recuperación < {condition}.')
        
        
        print('53. Actualizar observación para alumnos que hayan aprobado')
        DetalleNota.active_estudiante.filter(state=True, nota1__gte=5.0, nota2__gte=5.0).update(observacion='Aprobado')
        print('Se han actualizado las observaciones para estudiantes aprobados.')
        
        
        print('54. Actualizar todas las notas en un período específico')
        periodo=56
        DetalleNota.active_estudiante.filter(state=True, nota__periodo=periodo).update(nota1=10, nota2=10, recuperacion=10, observacion='Actualizado')
        print(f'Se han actualizado todas las notas en el período {periodo}.')
    def sentencias_delete():
        print('55. Eliminar físicamente todas las notas de un estudiante')
        estudiante_id = 56  # ID del estudiante a eliminar sus notas
        # Verificar si el estudiante existe
        if not Estudiante.objects.filter(id=estudiante_id).exists():
            print(f'No existe un estudiante con ID {estudiante_id}. No se realizó ninguna eliminación.')
        else:
            # Eliminar físicamente todas las notas del estudiante
            notas_eliminadas, _ = DetalleNota.objects.filter(estudiante_id=estudiante_id).delete()
            print(f'Se han eliminado físicamente {notas_eliminadas} notas del estudiante con ID {estudiante_id}') 
            
               
        print('56. Eliminar lógicamente todas las notas de un estudiante (en el campo state que indica si el registro está activo o no):')
        estudiante_id = 56  # ID del estudiante a eliminar lógicamente sus notas
        # Verificar si el estudiante existe
        if not Estudiante.objects.filter(id=estudiante_id).exists():
            print(f'No existe un estudiante con ID {estudiante_id}. No se realizó ninguna eliminación lógica.')
        else:
            # Actualizar el campo state a False para las notas del estudiante
            notas_actualizadas = DetalleNota.objects.filter(estudiante_id=estudiante_id).update(state=False)
            if notas_actualizadas > 0:
                print(f'Se han eliminado lógicamente {notas_actualizadas} notas del estudiante con ID {estudiante_id}')
            else:
                print(f'No se encontraron notas para eliminar lógicamente del estudiante con ID {estudiante_id}')

        
        print('57. Eliminar físicamente todas las notas de un período específico:')
        periodo_id = 55  # ID del período a eliminar físicamente sus notas
        # Obtener y eliminar físicamente todas las notas del período especificado
        notas_eliminadas = DetalleNota.objects.filter(nota__periodo_id=periodo_id).delete()
        if notas_eliminadas[0] > 0:
            print(f'Se han eliminado físicamente {notas_eliminadas[0]} notas del período con ID {periodo_id}')
        else:
            print(f'No se encontraron notas para eliminar físicamente del período con ID {periodo_id}')

        
        print('58. Eliminar lógicamente todas las notas de un período específico:')
        periodo_id = 55  # ID del período a eliminar lógicamente sus notas
        # Actualizar el campo state a False para las notas del período especificado
        notas_actualizadas = DetalleNota.objects.filter(nota__periodo_id=periodo_id).update(state=False)
        if notas_actualizadas > 0:
            print(f'Se han eliminado lógicamente {notas_actualizadas} notas del período con ID {periodo_id}')
        else:
            print(f'No se encontraron notas para eliminar lógicamente del período con ID {periodo_id}')

        
        print('59. Eliminar físicamente todas las notas que tengan una nota1 menor a 10:')
        valor = 10  # Valor límite para la nota1
        # Eliminar físicamente todas las notas donde nota1 sea menor que el valor especificado
        notas_eliminadas = DetalleNota.objects.filter(nota1__lt=valor).delete()
        if notas_eliminadas[0] > 0:
            print(f'Se han eliminado físicamente {notas_eliminadas[0]} notas con nota1 menor a {valor}')
        else:
            print(f'No se encontraron notas para eliminar físicamente con nota1 menor a {valor}')

        
        
    def crear_registro_de_notas():
            # Buscar o crear un estudiante de ejemplo
        estudiante, _ = Estudiante.objects.get_or_create(
            cedula='1234567890',  # Ejemplo de cédula
            nombre='Juan Pérez',  # Ejemplo de nombre
            user_id=1  # ID de usuario asociado (debe existir en tu base de datos)
        )
    
        # Obtener o crear un profesor de ejemplo
        profesor, _ = Profesor.objects.get_or_create(
            cedula='9876543210',  # Ejemplo de cédula
            nombre='María González',  # Ejemplo de nombre
            user_id=1  # ID de usuario asociado (debe existir en tu base de datos)
        )
    
        # Obtener o crear un periodo de ejemplo
        periodo, _ = Periodo.objects.get_or_create(
            periodo='2024 Primavera',  # Ejemplo de periodo
            user_id=1  # ID de usuario asociado (debe existir en tu base de datos)
        )
    
        # Obtener o crear una asignatura de ejemplo
        asignatura, _ = Asignatura.objects.get_or_create(
            description='Matemáticas',  # Ejemplo de descripción de asignatura
            user_id=1  # ID de usuario asociado (debe existir en tu base de datos)
        )
    
        # Crear una nueva nota para el estudiante
        nueva_nota = Nota.objects.create(
            profesor=profesor,
            periodo=periodo,
            asignatura=asignatura,
            user_id=1,  # ID de usuario asociado (debe existir en tu base de datos)
            created=datetime.now(),
            updated=datetime.now(),
            state=True  # Estado activo por defecto
        )
    
        # Crear un detalle de nota para la nueva nota y estudiante
        detalle_nota = DetalleNota.objects.create(
            estudiante=estudiante,
            nota=nueva_nota,
            nota1=8.5,  # Ejemplo de nota 1
            nota2=7.5,  # Ejemplo de nota 2
            recuperacion=6.0,  # Ejemplo de nota de recuperación
            observacion='Notas creadas como ejemplo',
            user_id=1,  # ID de usuario asociado (debe existir en tu base de datos)
            created=datetime.now(),
            updated=datetime.now(),
            state=True  # Estado activo por defecto
        )

        print(f'Se ha creado el registro de notas para el estudiante {estudiante.nombre}. DetalleNota ID: {detalle_nota.id}')
        
    crear_registro_de_notas()
        
        
        
        
        
      
      
          
    
    # sentencias_delete()
if __name__ == '__main__':
    probar_orm()