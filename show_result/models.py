from django.db import models

class PeriodoTiempo(models.Model):
    idperiodo_tiempo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    def _str_(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Periodos Tiempo'
        db_table = 'Periodo_Tiempo'
        ordering = ['idperiodo_tiempo']

class TipoPlanta(models.Model):
    idtipo_planta = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    def _str_(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Tipos Plantas'
        db_table = 'Tipo_Planta'
        ordering = ['idtipo_planta']

class Planta(models.Model):
    idplanta = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    idtipo_planta = models.ForeignKey(TipoPlanta, on_delete=models.CASCADE, verbose_name='Tipo de Planta')

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Plantas'
        db_table = 'Planta'
        ordering = ['idplanta']

class Plaga(models.Model):
    idplaga = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Plagas'
        db_table = 'Plaga'
        ordering = ['idplaga']

class Resultado(models.Model):
    idresultado = models.IntegerField(primary_key=True)
    fecha_hora = models.DateField(verbose_name='Fecha y Hora')
    idplaga = models.ForeignKey(Plaga, on_delete=models.CASCADE, verbose_name='Plaga')
    idregistro = models.IntegerField(verbose_name='ID Registro')
    idplanta = models.ForeignKey(Planta, on_delete=models.CASCADE, verbose_name='Planta')

    def _str_(self):
        return f"Resultado-{self.idresultado}"

    class Meta:
        verbose_name_plural = 'Resultados'
        db_table = 'Resultado'
        ordering = ['idresultado']

class Producto(models.Model):
    idproducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    idmarca = models.IntegerField(verbose_name='ID Marca')

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['idproducto']

class DetalleResultado(models.Model):
    id_detalle_result = models.IntegerField(primary_key=True)
    idresultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, verbose_name='Resultado')
    idproducto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    idperiodo_tiempo = models.ForeignKey(PeriodoTiempo, on_delete=models.CASCADE, verbose_name='Periodo Tiempo')

    def _str_(self):
        return f"DetalleResultado-{self.id_detalle_result}"

    class Meta:
        verbose_name_plural = 'Detalles Resultados'
        db_table = 'Detalle_Resultado'
        ordering = ['id_detalle_result']

class Marca(models.Model):
    idmarca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Marcas'
        db_table = 'Marca'
        ordering = ['idmarca']